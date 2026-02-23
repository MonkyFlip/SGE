from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base compartido
class TutoriaBaseSchema(BaseModel):
    tutor_id: int
    estudiante_id: int
    fecha: datetime
    canalizado: bool = False
    descripcion: Optional[str] = None
    acciones: Optional[str] = None
    tipo: str


# Crear tutoría
class TutoriaCreateSchema(TutoriaBaseSchema):
    pass


# Actualizar tutoría (parcial)
class TutoriaUpdateSchema(BaseModel):
    fecha: Optional[datetime] = None
    estado: Optional[str] = None
    canalizado: Optional[bool] = None
    descripcion: Optional[str] = None
    acciones: Optional[str] = None
    tipo: Optional[str] = None


# Respuesta
class TutoriaResponseSchema(TutoriaBaseSchema):
    id_tutoria: int
    estado: str

    class Config:
        from_attributes = True
