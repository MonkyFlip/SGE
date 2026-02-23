from pydantic import BaseModel


# Base compartido
class GrupoTutorBaseSchema(BaseModel):
    nombre: str


# Crear GrupoTutor
class GrupoTutorCreateSchema(GrupoTutorBaseSchema):
    nombre: str


# Actualizar GrupoTutor
class GrupoTutorUpdateSchema(BaseModel):
    nombre: str


# Respuesta
class GrupoTutorResponseSchema(GrupoTutorBaseSchema):
    id_genero: int

    class Config:
        from_attributes = True