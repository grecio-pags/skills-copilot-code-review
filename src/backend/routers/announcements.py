"""
Announcements endpoints for the High School Management System API
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from ..database import announcements_collection, teachers_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


class AnnouncementCreate(BaseModel):
    message: str = Field(min_length=5, max_length=500)
    expires_at: datetime
    starts_at: Optional[datetime] = None


class AnnouncementUpdate(BaseModel):
    message: Optional[str] = Field(default=None, min_length=5, max_length=500)
    expires_at: Optional[datetime] = None
    starts_at: Optional[datetime] = None


def normalize_datetime(value: Optional[datetime]) -> Optional[datetime]:
    """Convert datetimes to UTC naive so MongoDB reads/writes stay comparable."""
    if value is None:
        return None
    if value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)


def utc_now_naive() -> datetime:
    """Return current UTC datetime without timezone information."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def require_authenticated_teacher(teacher_username: Optional[str]) -> Dict[str, Any]:
    """Validate teacher identity for write operations."""
    if not teacher_username:
        raise HTTPException(status_code=401, detail="Authentication required")

    teacher = teachers_collection.find_one({"_id": teacher_username})
    if not teacher:
        raise HTTPException(status_code=401, detail="Invalid teacher credentials")

    return teacher


def serialize_announcement(doc: Dict[str, Any], now: datetime) -> Dict[str, Any]:
    """Serialize announcement document for API responses."""
    starts_at = normalize_datetime(doc.get("starts_at"))
    expires_at = normalize_datetime(doc.get("expires_at"))

    is_active = bool(
        expires_at and expires_at > now and (starts_at is None or starts_at <= now)
    )

    return {
        "id": str(doc["_id"]),
        "message": doc["message"],
        "starts_at": starts_at,
        "expires_at": expires_at,
        "created_at": doc.get("created_at"),
        "updated_at": doc.get("updated_at"),
        "is_active": is_active
    }


@router.get("", response_model=List[Dict[str, Any]])
@router.get("/", response_model=List[Dict[str, Any]])
def list_announcements() -> List[Dict[str, Any]]:
    """List all announcements ordered by expiration and creation date."""
    now = utc_now_naive()
    announcements: List[Dict[str, Any]] = []

    cursor = announcements_collection.find({}).sort([
        ("expires_at", 1),
        ("created_at", -1)
    ])

    for announcement in cursor:
        announcements.append(serialize_announcement(announcement, now))

    return announcements


@router.get("/active", response_model=List[Dict[str, Any]])
def list_active_announcements() -> List[Dict[str, Any]]:
    """List only active announcements for public display."""
    now = utc_now_naive()

    query: Dict[str, Any] = {
        "expires_at": {"$gt": now},
        "$or": [
            {"starts_at": None},
            {"starts_at": {"$exists": False}},
            {"starts_at": {"$lte": now}}
        ]
    }

    announcements: List[Dict[str, Any]] = []
    cursor = announcements_collection.find(query).sort([
        ("starts_at", -1),
        ("created_at", -1)
    ])

    for announcement in cursor:
        announcements.append(serialize_announcement(announcement, now))

    return announcements


@router.post("", response_model=Dict[str, Any], status_code=201)
def create_announcement(
    payload: AnnouncementCreate,
    teacher_username: Optional[str] = Query(None)
) -> Dict[str, Any]:
    """Create a new announcement. Only logged-in teachers can perform this action."""
    require_authenticated_teacher(teacher_username)

    starts_at = normalize_datetime(payload.starts_at)
    expires_at = normalize_datetime(payload.expires_at)
    message = payload.message.strip()

    if len(message) < 5:
        raise HTTPException(
            status_code=400,
            detail="Announcement message must contain at least 5 characters"
        )

    if starts_at and expires_at <= starts_at:
        raise HTTPException(
            status_code=400,
            detail="Expiration date must be later than start date"
        )

    now = utc_now_naive()
    new_doc = {
        "message": message,
        "starts_at": starts_at,
        "expires_at": expires_at,
        "created_at": now,
        "updated_at": now
    }

    inserted = announcements_collection.insert_one(new_doc)
    created = announcements_collection.find_one({"_id": inserted.inserted_id})

    if not created:
        raise HTTPException(status_code=500, detail="Failed to create announcement")

    return serialize_announcement(created, now)


@router.put("/{announcement_id}", response_model=Dict[str, Any])
def update_announcement(
    announcement_id: str,
    payload: AnnouncementUpdate,
    teacher_username: Optional[str] = Query(None)
) -> Dict[str, Any]:
    """Update an existing announcement. Only logged-in teachers can perform this action."""
    require_authenticated_teacher(teacher_username)

    try:
        object_id = ObjectId(announcement_id)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid announcement id") from exc

    existing = announcements_collection.find_one({"_id": object_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Announcement not found")

    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    if "message" in updates and updates["message"] is not None:
        updates["message"] = updates["message"].strip()
        if len(updates["message"]) < 5:
            raise HTTPException(
                status_code=400,
                detail="Announcement message must contain at least 5 characters"
            )

    if "starts_at" in updates:
        updates["starts_at"] = normalize_datetime(updates["starts_at"])

    if "expires_at" in updates and updates["expires_at"] is not None:
        updates["expires_at"] = normalize_datetime(updates["expires_at"])

    final_starts_at = updates.get("starts_at", existing.get("starts_at"))
    final_expires_at = updates.get("expires_at", existing.get("expires_at"))

    if final_starts_at and final_expires_at <= final_starts_at:
        raise HTTPException(
            status_code=400,
            detail="Expiration date must be later than start date"
        )

    updates["updated_at"] = utc_now_naive()

    result = announcements_collection.update_one(
        {"_id": object_id},
        {"$set": updates}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Announcement not found")

    updated = announcements_collection.find_one({"_id": object_id})
    if not updated:
        raise HTTPException(status_code=500, detail="Failed to load announcement")

    return serialize_announcement(updated, utc_now_naive())


@router.delete("/{announcement_id}", response_model=Dict[str, str])
def delete_announcement(
    announcement_id: str,
    teacher_username: Optional[str] = Query(None)
) -> Dict[str, str]:
    """Delete an announcement. Only logged-in teachers can perform this action."""
    require_authenticated_teacher(teacher_username)

    try:
        object_id = ObjectId(announcement_id)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid announcement id") from exc

    result = announcements_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Announcement not found")

    return {"message": "Announcement deleted successfully"}
