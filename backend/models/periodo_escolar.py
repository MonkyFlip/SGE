from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import relationship
from datetime import date
from base import Base

class PeriodoE(Base):
    __tablename__ = 'periodo_escolar'

    # Campos principales
    id_periodo = Column(Integer, primary_key=True, autoincrement=True)

    alias = Column(String(50), unique=True, nullable=False)
    inicio = Column(date.now(), nullable=False)
    fin = Column(date.now(), nullable=False)
    activo = Column(Boolean, default=False)

    # Relaciones
    carrera = relationship("Carreras", back_populates="periodo")