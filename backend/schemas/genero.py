from pydantic import BaseModel
from typing import Optional


# Base compartido
class GeneroBaseSchema(BaseModel):
    nombre: str


# Crear género
class GeneroCreateSchema(GeneroBaseSchema):
    pass


# Actualizar género (parcial)
class GeneroUpdateSchema(BaseModel):
    nombre: Optional[str] = None


# Respuesta
class GeneroResponseSchema(GeneroBaseSchema):
    id_genero: int

    class Config:
        from_attributes = True
