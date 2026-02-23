from pydantic import BaseModel


# Base compartido
class CarrerasBaseSchema(BaseModel):
    periodo_id: int
    alias: str
    inicio: str
    fin: str


# Crear Carreras
class CarrerasCreateSchema(CarrerasBaseSchema):
    periodo_id: int
    alias: str
    inicio: str
    fin: str


# Actualizar Carreras
class CarrerasUpdateSchema(BaseModel):
    alias: str
    inicio: str
    fin: str


# Respuesta
class CarrerasResponseSchema(CarrerasBaseSchema):
    id_carrera: int

    class Config:
        from_attributes = True