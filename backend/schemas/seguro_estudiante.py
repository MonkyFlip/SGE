from pydantic import BaseModel


# Base compartido
class SeguroEstudianteBaseSchema(BaseModel):
    seguro_med_id: int
    estudiante_id: int
    nss: str
    estatus: bool
    clinica: str
    activo: bool


# Crear SeguroEstudiante
class SeguroEstudianteCreateSchema(SeguroEstudianteBaseSchema):
    seguro_med_id: int
    estudiante_id: int
    nss: str
    estatus: bool
    clinica: str
    activo: bool


# Actualizar SeguroEstudiante
class SeguroEstudianteUpdateSchema(BaseModel):
    nss: str
    estatus: bool
    clinica: str
    activo: bool


# Respuesta
class SeguroEstudianteResponseSchema(SeguroEstudianteBaseSchema):
    id_seguro_est: int

    class Config:
        from_attributes = True