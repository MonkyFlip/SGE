from pydantic import BaseModel
from typing import Optional


# Base compartido
class GrupoTutorBaseSchema(BaseModel):
    grupo_id: int
    tutor_id: int


# Crear asignación grupo–tutor
class GrupoTutorCreateSchema(GrupoTutorBaseSchema):
    pass


# Actualizar asignación (parcial)
class GrupoTutorUpdateSchema(BaseModel):
    activo: Optional[bool] = None


# Respuesta
class GrupoTutorResponseSchema(GrupoTutorBaseSchema):
    id_grupo_tutor: int
    activo: bool

    class Config:
        from_attributes = True
