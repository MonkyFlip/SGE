from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Grupos(Base):
    __tablename__ = 'grupos'

    # Campos principales
    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    carrera_id = Column(Integer, ForeignKey("carrera.id_carrera"), nullable=False)

    nombre = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False, default=True)

    # Relaciones
    carrera = relationship("Carreras", back_populates="grupos")
    grupo_tutor = relationship("GrupoTutor", back_populates="grupos")