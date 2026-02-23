from pydantic import BaseModel


# Base compartido
class PeriodoEscolarBaseSchema(BaseModel):
    alias: str
    inicio: str
    fin: str
    activo: bool


# Crear PeriodoEscolar
class PeriodoEscolarCreateSchema(PeriodoEscolarBaseSchema):
    alias: str
    inicio: str
    fin: str
    activo: bool


# Actualizar PeriodoEscolar
class PeriodoEscolarUpdateSchema(BaseModel):
    inicio: str
    fin: str
    activo: bool


# Respuesta
class PeriodoEscolarResponseSchema(PeriodoEscolarBaseSchema):
    id_periodo: int

    class Config:
        from_attributes = True