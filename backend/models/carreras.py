from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

class Carreras(Base):
    __tablename__ = 'carrera'

    id_carrera = Column(Integer, primary_key=True, autoincrement=True)
    periodo_id = Column(Integer, ForeignKey('periodo_escolar.id_periodo'), nullable=False)

    alias = Column(String(50), nullable=False)
    inicio = Column(DateTime(timezone=True), nullable=False)
    fin = Column(DateTime(timezone=True), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)

    # Relaciones
    periodo = relationship("PeriodoEscolar", back_populates="carrera")
    grupos = relationship("Grupos", back_populates="carrera")
