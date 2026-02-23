from pydantic import BaseModel
from typing import Optional


# Base compartido
class SeguroEstudianteBaseSchema(BaseModel):
    seguro_med_id: int
    estudiante_id: int
    nss: str
    clinica: str


# Crear seguro del estudiante
class SeguroEstudianteCreateSchema(SeguroEstudianteBaseSchema):
    pass


# Actualizar seguro del estudiante (parcial)
class SeguroEstudianteUpdateSchema(BaseModel):
    nss: Optional[str] = None
    clinica: Optional[str] = None
    activo: Optional[bool] = None


# Respuesta
class SeguroEstudianteResponseSchema(SeguroEstudianteBaseSchema):
    id_seguro_est: int
    activo: bool

    class Config:
        from_attributes = True
