from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import relationship
from base import Base

class GrupoTutor(Base):
    __tablename__ = 'grupo_tutor'

    # Campos principales
    id_grupo_tutor = Column(Integer, primary_key=True, nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupos.id_grupo"), nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id_tutor"), nullable=False)

    # Relaciones
    grupos = relationship("Grupos", back_populates="grupo_tutor")
    tutores = relationship("Tutores", back_populates="grupo_tutor")
