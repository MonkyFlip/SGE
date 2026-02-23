from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base compartido
class CarrerasBaseSchema(BaseModel):
    periodo_id: int
    alias: str
    inicio: datetime
    fin: datetime


# Crear carrera
class CarrerasCreateSchema(CarrerasBaseSchema):
    pass


# Actualizar carrera (parcial)
class CarrerasUpdateSchema(BaseModel):
    alias: Optional[str] = None
    inicio: Optional[datetime] = None
    fin: Optional[datetime] = None
    activo: Optional[bool] = None


# Respuesta
class CarrerasResponseSchema(CarrerasBaseSchema):
    id_carrera: int
    activo: bool

    class Config:
        from_attributes = True
