from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base compartido
class SoliPsicopedagogiaBaseSchema(BaseModel):
    tutor_id: int
    estudiante_id: int
    fecha_lugar: str
    tipo_servicio: str
    quien_canaliza: str
    motivo: str
    observaciones: Optional[str] = None
    archivo_pdf: Optional[str] = None


# Crear solicitud
class SoliPsicopedagogiaCreateSchema(SoliPsicopedagogiaBaseSchema):
    pass


# Actualizar solicitud (parcial)
class SoliPsicopedagogiaUpdateSchema(BaseModel):
    fecha_lugar: Optional[str] = None
    tipo_servicio: Optional[str] = None
    quien_canaliza: Optional[str] = None
    motivo: Optional[str] = None
    observaciones: Optional[str] = None
    estado: Optional[str] = None
    archivo_pdf: Optional[str] = None


# Respuesta
class SoliPsicopedagogiaResponseSchema(SoliPsicopedagogiaBaseSchema):
    id_solicitud: int
    fecha_soli: datetime
    estado: str

    class Config:
        from_attributes = True
