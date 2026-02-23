from pydantic import BaseModel


# Base compartido
class GruposBaseSchema(BaseModel):
    carrera_id: int
    nombre: str
    activo: bool


# Crear Grupos
class GruposCreateSchema(GruposBaseSchema):
    carrera_id: int
    nombre: str
    activo: bool


# Actualizar Grupos
class GruposUpdateSchema(BaseModel):
    nombre: str
    activo: bool


# Respuesta
class GruposResponseSchema(GruposBaseSchema):
    id_grupo: int

    class Config:
        from_attributes = True