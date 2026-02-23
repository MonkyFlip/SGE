from pydantic import BaseModel
from typing import Optional


# Base compartido
class GruposBaseSchema(BaseModel):
    carrera_id: int
    nombre: str


# Crear grupo
class GruposCreateSchema(GruposBaseSchema):
    pass


# Actualizar grupo (parcial)
class GruposUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    activo: Optional[bool] = None


# Respuesta
class GruposResponseSchema(GruposBaseSchema):
    id_grupo: int
    activo: bool

    class Config:
        from_attributes = True
