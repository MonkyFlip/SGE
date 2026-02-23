from pydantic import BaseModel
from typing import Optional


# Base compartido
class EstudianteGrupoBaseSchema(BaseModel):
    estudiante_id: int
    grupo_id: int


# Crear asignación estudiante–grupo
class EstudianteGrupoCreateSchema(EstudianteGrupoBaseSchema):
    pass


# Actualizar asignación (parcial)
class EstudianteGrupoUpdateSchema(BaseModel):
    grupo_id: Optional[int] = None
    activo: Optional[bool] = None


# Respuesta
class EstudianteGrupoResponseSchema(EstudianteGrupoBaseSchema):
    id_est_grupo: int
    activo: bool

    class Config:
        from_attributes = True
