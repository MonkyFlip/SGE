from pydantic import BaseModel
from typing import Optional


# Base compartido
class UsuarioBaseSchema(BaseModel):
    rol_id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    email: str
    password: str
    email_verified: bool
    email_verified_at: bool
    created_at: str
    updated_at: str
    estado: str


# Crear usuario
class UsuarioCreateSchema(UsuarioBaseSchema):
    rol_id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    email: str
    password: str
    estado: str


# Actualziar usuario
class UsuarioUpdateSchema(BaseModel):
    rol_id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    email: str
    password: str
    estado: str


# Respuesta
class UsuarioResponseSchema(UsuarioBaseSchema):
    id_usuario: int

    class Config:
        from_attributes = True