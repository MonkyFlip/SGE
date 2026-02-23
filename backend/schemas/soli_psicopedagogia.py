from pydantic import BaseModel
from typing import Optional


# Base compartido
class SoliPsicopedagogiaBaseSchema(BaseModel):
    tutor_id: int
    estudiante_id: str
    fecha_soli: str
    fecha_lugar: str
    tipo_servicio: str
    quien_canaliza: str
    motivo: str
    observaciones: str
    estado: str
    archivo_pdf: Optional[str] = None


# Crear SoliPsicopedagogia
class SoliPsicopedagogiaCreateSchema(SoliPsicopedagogiaBaseSchema):
    tutor_id: int
    estudiante_id: str
    fecha_soli: str
    fecha_lugar: str
    tipo_servicio: str
    quien_canaliza: str
    motivo: str
    observaciones: str
    estado: str
    archivo_pdf: Optional[str] = None


# Actualizar SoliPsicopedagogia
class SoliPsicopedagogiaUpdateSchema(BaseModel):
    fecha_soli: str
    fecha_lugar: str
    tipo_servicio: str
    quien_canaliza: str
    motivo: str
    observaciones: str
    estado: str
    archivo_pdf: Optional[str] = None


# Respuesta
class SoliPsicopedagogiaResponseSchema(SoliPsicopedagogiaBaseSchema):
    id_solicitud: int

    class Config:
        from_attributes = True