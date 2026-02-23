from pydantic import BaseModel


# Base compartido
class EstudianteGrupoBaseSchema(BaseModel):
    estudiante_id: int
    grupo_id: int
    activo: str


# Crear EstudianteGrupo
class EstudianteGrupoCreateSchema(EstudianteGrupoBaseSchema):
    estudiante_id: int
    grupo_id: int
    activo: str


# Actualizar EstudianteGrupo
class EstudianteGrupoUpdateSchema(BaseModel):
    grupo_id: int
    activo: str


# Respuesta
class EstudianteGrupoResponseSchema(EstudianteGrupoBaseSchema):
    id_est_grupo: int

    class Config:
        from_attributes = True