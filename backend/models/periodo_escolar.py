from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import date
from database import Base

class PeriodoEscolar(Base):
    __tablename__ = 'periodo_escolar'

    # Campos principales
    id_periodo = Column(Integer, primary_key=True, autoincrement=True)

    alias = Column(String(50), nullable=False)
    inicio = Column(DateTime(timezone=True), nullable=False)
    fin = Column(DateTime(timezone=True), nullable=False)
    activo = Column(Boolean, default=False)

    # Relaciones
    carrera = relationship("Carreras", back_populates="periodo")