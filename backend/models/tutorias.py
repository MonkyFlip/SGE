from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Tutorias(Base):
    __tablename__ = 'tutorias'

    # Campos principales
    id_tutoria = Column(Integer, primary_key=True, autoincrement=True)
    tutor_id = Column(Integer, ForeignKey('tutores.id_tutor'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id_estudiante'), nullable=False)
    fecha = Column(DateTime(timezone=True), nullable=False)
    estado = Column(String(20), nullable=False, default="ABIERTA")
    canalizado = Column(Boolean, default=False)
    descripcion = Column(String(255), nullable=True)
    acciones = Column(String(255), nullable=True)
    tipo = Column(String(50), nullable=False)  # Ejemplo: "Académica", "Psicológica", etc.

    # Relaciones
    tutor = relationship("Tutores", back_populates="tutorias")
    estudiante = relationship("Estudiantes", back_populates="tutorias")