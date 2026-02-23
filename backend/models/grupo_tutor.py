from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class GrupoTutor(Base):
    __tablename__ = 'grupo_tutor'

    # Campos principales
    id_grupo_tutor = Column(Integer, primary_key=True, nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupos.id_grupo"), nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id_tutor"), nullable=False)

    activo = Column(Boolean, nullable=False, default=True)

    # Relaciones
    grupos = relationship("Grupos", back_populates="grupo_tutor")
    tutores = relationship("Tutores", back_populates="grupo_tutor")
