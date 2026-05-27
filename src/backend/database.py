"""
MongoDB database configuration and setup for Mergington High School API
"""

from pymongo import MongoClient
from argon2 import PasswordHasher, exceptions as argon2_exceptions

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mergington_high']
activities_collection = db['activities']
teachers_collection = db['teachers']

# Methods


def hash_password(password):
    """Hash password using Argon2"""
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    """Verify a plain password against an Argon2 hashed password.

    Returns True when the password matches, False otherwise.
    """
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except argon2_exceptions.VerifyMismatchError:
        return False
    except Exception:
        # For any other exception (e.g., invalid hash), treat as non-match
        return False


def init_database():
    """Initialize database if empty"""

    # Initialize activities if empty
    if activities_collection.count_documents({}) == 0:
        for name, details in initial_activities.items():
            activities_collection.insert_one({"_id": name, **details})

    # Initialize teacher accounts if empty
    if teachers_collection.count_documents({}) == 0:
        for teacher in initial_teachers:
            teachers_collection.insert_one(
                {"_id": teacher["username"], **teacher})


# Initial database if empty
initial_activities = {
    "Clube de Xadrez": {
        "description": "Aprenda estratégias e dispute torneios de xadrez",
        "schedule": "Segundas e sextas, 15:15 - 16:45",
        "schedule_details": {
            "days": ["Segunda", "Sexta"],
            "start_time": "15:15",
            "end_time": "16:45"
        },
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Aula de Programação": {
        "description": "Aprenda fundamentos de programação e desenvolva projetos de software",
        "schedule": "Terças e quintas, 07:00 - 08:00",
        "schedule_details": {
            "days": ["Terça", "Quinta"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Treino Matinal": {
        "description": "Treinamento físico e exercícios no início da manhã",
        "schedule": "Segundas, quartas e sextas, 06:30 - 07:45",
        "schedule_details": {
            "days": ["Segunda", "Quarta", "Sexta"],
            "start_time": "06:30",
            "end_time": "07:45"
        },
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Time de Futebol": {
        "description": "Participe do time de futebol da escola e dispute partidas",
        "schedule": "Terças e quintas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Terça", "Quinta"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Time de Basquete": {
        "description": "Treine e dispute torneios de basquete",
        "schedule": "Quartas e sextas, 15:15 - 17:00",
        "schedule_details": {
            "days": ["Quarta", "Sexta"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Clube de Arte": {
        "description": "Explore técnicas de arte e crie obras-primas",
        "schedule": "Quintas, 15:15 - 17:00",
        "schedule_details": {
            "days": ["Quinta"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Clube de Teatro": {
        "description": "Atue, dirija e produza peças e apresentações",
        "schedule": "Segundas e quartas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Segunda", "Quarta"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Clube de Matemática": {
        "description": "Resolva desafios e prepare-se para olimpíadas de matemática",
        "schedule": "Terças, 07:15 - 08:00",
        "schedule_details": {
            "days": ["Terça"],
            "start_time": "07:15",
            "end_time": "08:00"
        },
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Equipe de Debate": {
        "description": "Desenvolva habilidades de oratória e argumentação",
        "schedule": "Sextas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Sexta"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"]
    },
    "Oficina de Robótica (Final de Semana)": {
        "description": "Monte e programe robôs em nosso laboratório moderno",
        "schedule": "Sábados, 10:00 - 14:00",
        "schedule_details": {
            "days": ["Sábado"],
            "start_time": "10:00",
            "end_time": "14:00"
        },
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "oliver@mergington.edu"]
    },
    "Olimpíada de Ciências": {
        "description": "Preparação para competições científicas regionais e estaduais no fim de semana",
        "schedule": "Sábados, 13:00 - 16:00",
        "schedule_details": {
            "days": ["Sábado"],
            "start_time": "13:00",
            "end_time": "16:00"
        },
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
    },
    "Torneio de Xadrez (Domingo)": {
        "description": "Torneio semanal para enxadristas com ranking",
        "schedule": "Domingos, 14:00 - 17:00",
        "schedule_details": {
            "days": ["Domingo"],
            "start_time": "14:00",
            "end_time": "17:00"
        },
        "max_participants": 16,
        "participants": ["william@mergington.edu", "jacob@mergington.edu"]
    }
}

initial_teachers = [
    {
        "username": "mrodriguez",
        "display_name": "Profa. Rodriguez",
        "password": hash_password("art123"),
        "role": "teacher"
    },
    {
        "username": "mchen",
        "display_name": "Prof. Chen",
        "password": hash_password("chess456"),
        "role": "teacher"
    },
    {
        "username": "principal",
        "display_name": "Diretora Martinez",
        "password": hash_password("admin789"),
        "role": "admin"
    }
]
