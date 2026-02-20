# Sistema de Gestión Escolar

## Migraciones con alembic
```bash
alembic init alembic
alembic revision --autogenerate -m "init"
alembic upgrade head
```