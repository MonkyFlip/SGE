from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import relationship
from datetime import date
from base import Base

class Carreras(Base):
    __tablename__ = 'carrera'

    # Campos principales
    id_carrera = Column(Integer, primary_key=True, autoincrement=True)
    periodo_id = Column(Integer, ForeignKey('periodo_escolar.id_periodo'), nullable=False)

    alias = Column(String(50), unique=True, nullable=False)
    inicio = Column(date.now(), nullable=False)
    fin = Column(date.now(), nullable=False)
    activo = Column(Boolean, default=False)

    # Relaciones
    periodo = relationship("PeriodoE", back_populates="carrera")
    grupos = relationship("Grupos", back_populates="carrera")
