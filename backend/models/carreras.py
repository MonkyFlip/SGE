from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import date
from database import Base

class Carreras(Base):
    __tablename__ = 'carrera'

    # Campos principales
    id_carrera = Column(Integer, primary_key=True, autoincrement=True)
    periodo_id = Column(Integer, ForeignKey('periodo_escolar.id_periodo'), nullable=False)

    alias = Column(String(50), unique=True, nullable=False)
    inicio = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable=False)
    activo = Column(Boolean, default=False)

    # Relaciones
    periodo = relationship("PeriodoEscolar", back_populates="carrera")
    grupos = relationship("Grupos", back_populates="carrera")
