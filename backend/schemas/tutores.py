from pydantic import BaseModel


# Base compartido
class TutorBaseSchema(BaseModel):
    usuario_id: int
    clave_sp: str
    telefono: str
    estado: str


# Crear Tutor
class TutorCreateSchema(TutorBaseSchema):
    usuario_id: int
    clave_sp: str
    telefono: str
    estado: str


# Actualizar Tutor
class TutorUpdateSchema(BaseModel):
    clave_sp: str
    telefono: str
    estado: str


# Respuesta
class TutorResponseSchema(TutorBaseSchema):
    id_tutor: int

    class Config:
        from_attributes = True