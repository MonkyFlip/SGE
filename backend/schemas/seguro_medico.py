from pydantic import BaseModel


# Base compartido
class SeguroMedicoBaseSchema(BaseModel):
    nombre: str


# Crear SeguroMedico
class SeguroMedicoCreateSchema(SeguroMedicoBaseSchema):
    nombre: str


# Actualizar SeguroMedico
class SeguroMedicoUpdateSchema(BaseModel):
    nombre: str


# Respuesta
class SeguroMedicoResponseSchema(SeguroMedicoBaseSchema):
    id_seguro_med: int

    class Config:
        from_attributes = True