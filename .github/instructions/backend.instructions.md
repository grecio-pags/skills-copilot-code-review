---
applyTo: "backend/**/*,*.py"
---

## Diretrizes de Backend

- Todos os endpoints de API devem ser definidos na pasta `routers`.
- Carregue conteúdo de exemplo do banco de dados a partir do arquivo `database.py`.
- O tratamento de erros deve ser registrado apenas no servidor. Não propague para o frontend.
- Garanta que todas as APIs estejam explicadas na documentação.
- Verifique se mudanças no backend se refletem no frontend (`src/static/**`). Se encontrar possíveis breaking changes, mencione ao desenvolvedor.