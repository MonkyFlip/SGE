from pydantic import BaseModel


# Base compartido
class EstudiantesBaseSchema(BaseModel):
    usuario_id: int
    genero_id: int
    matricula: str
    telefono: str
    estado: str


# Crear Estudiantes
class EstudiantesCreateSchema(EstudiantesBaseSchema):
    usuario_id: int
    genero_id: int
    matricula: str
    telefono: str
    estado: str


# Actualizar Estudiantes
class EstudiantesUpdateSchema(BaseModel):
    genero_id: int  # Por si el chavo me sale raro
    matricula: str  # Por si se comete un error
    telefono: str
    estado: str


# Respuesta
class EstudiantesResponseSchema(EstudiantesBaseSchema):
    id_estudiante: int

    class Config:
        from_attributes = True