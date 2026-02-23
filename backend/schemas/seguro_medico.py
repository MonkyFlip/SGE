from pydantic import BaseModel
from typing import Optional


# Base compartido
class SeguroMedicoBaseSchema(BaseModel):
    nombre: str


# Crear seguro médico
class SeguroMedicoCreateSchema(SeguroMedicoBaseSchema):
    pass


# Actualizar seguro médico (parcial)
class SeguroMedicoUpdateSchema(BaseModel):
    nombre: Optional[str] = None


# Respuesta
class SeguroMedicoResponseSchema(SeguroMedicoBaseSchema):
    id_seguro_med: int

    class Config:
        from_attributes = True
