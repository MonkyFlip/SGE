from pydantic import BaseModel
from typing import Optional


# Base compartido
class TutoriaBaseSchema(BaseModel):
    tutor_id: int
    estudiante_id: int
    fecha: str
    estado: str
    canalizado: bool
    descripcion: Optional[str] = None
    acciones: str
    tipo: str


# Crear tutoria
class TutoriaCreateSchema(TutoriaBaseSchema):
    tutor_id: int
    estudiante_id: int
    fecha: str
    estado: str
    canalizado: bool
    descripcion: Optional[str] = None
    acciones: str
    tipo: str


# Actualizar tutoria
class TutoriaUpdateSchema(BaseModel):
    fecha: str
    estado: str
    canalizado: bool
    descripcion: Optional[str] = None
    acciones: str
    tipo: str


# Respuesta
class TutoriaResponseSchema(TutoriaBaseSchema):
    id_tutoria: int

    class Config:
        from_attributes = True