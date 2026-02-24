from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base compartido
class UsuarioBaseSchema(BaseModel):
    rol_id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    email: str


# Crear usuario
class UsuarioCreateSchema(UsuarioBaseSchema):
    password: str


# Actualizar usuario (parcial)
class UsuarioUpdateSchema(BaseModel):
    rol_id: Optional[int] = None
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


# Respuesta
class UsuarioResponseSchema(UsuarioBaseSchema):
    id_usuario: int
    email_verified: bool
    email_verified_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    estado: str

    class Config:
        from_attributes = True
