from pydantic import BaseModel
from typing import Optional


# Base compartido
class TutorBaseSchema(BaseModel):
    usuario_id: int
    clave_sp: int
    telefono: Optional[str] = None


# Crear tutor
class TutorCreateSchema(TutorBaseSchema):
    pass


# Actualizar tutor (parcial)
class TutorUpdateSchema(BaseModel):
    clave_sp: Optional[int] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None


# Respuesta
class TutorResponseSchema(TutorBaseSchema):
    id_tutor: int
    estado: str

    class Config:
        from_attributes = True
