from pydantic import BaseModel
from typing import Optional


# Base compartido
class EstudiantesBaseSchema(BaseModel):
    usuario_id: int
    genero_id: int
    matricula: str
    telefono: str


# Crear estudiante
class EstudiantesCreateSchema(EstudiantesBaseSchema):
    pass


# Actualizar estudiante (parcial)
class EstudiantesUpdateSchema(BaseModel):
    genero_id: Optional[int] = None
    matricula: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None


# Respuesta
class EstudiantesResponseSchema(EstudiantesBaseSchema):
    id_estudiante: int
    estado: str

    class Config:
        from_attributes = True
