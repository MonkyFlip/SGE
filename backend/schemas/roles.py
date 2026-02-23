from pydantic import BaseModel
from typing import Optional


# Base compartido
class RolBaseSchema(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


# Crear rol
class RolCreateSchema(RolBaseSchema):
    pass


# Actualizar rol
class RolUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


# Respuesta
class RolResponseSchema(RolBaseSchema):
    id_rol: int

    class Config:
        from_attributes = True
