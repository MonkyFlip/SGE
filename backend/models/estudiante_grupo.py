from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class EstudianteGrupo(Base):
    __tablename__ = 'estudiante_grupo'

    id_est_grupo = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupos.id_grupo"), nullable=False)

    # Estado de la asignación
    activo = Column(Boolean, nullable=False, default=True)

    # Relaciones
    grupos = relationship("Grupos", back_populates="estudiante_grupo")
    estudiantes = relationship("Estudiantes", back_populates="estudiante_grupo")
