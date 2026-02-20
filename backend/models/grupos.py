from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import relationship
from datetime import date
from base import Base

class Grupos(Base):
    __tablename__ = 'grupos'

    # Campos principales
    id_grupo = Column(Integer, primary_key=True, nullable=False)
    carrera_id = Column(Integer, ForeignKey("carrera.id_carrera"), nullable=False)

    nombre = Column(String(50), unique=True, nullable=False)
    activo = Column(Boolean, default=False)

    # Relaciones
    carrera = relationship("Carreras", back_populates="grupos")
    grupo_tutor = relationship("GrupoTutor", back_populates="grupos")