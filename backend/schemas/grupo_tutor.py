from pydantic import BaseModel


# Base compartido
class GrupoTutorBaseSchema(BaseModel):
    grupo_id: int
    tutor_id: int
    activo: bool


# Crear GrupoTutor
class GrupoTutorCreateSchema(GrupoTutorBaseSchema):
    grupo_id: int
    tutor_id: int
    activo: bool


# Actualizar GrupoTutor
class GrupoTutorUpdateSchema(BaseModel):
    activo: bool


# Respuesta
class GrupoTutorResponseSchema(GrupoTutorBaseSchema):
    id_grupo: int

    class Config:
        from_attributes = True