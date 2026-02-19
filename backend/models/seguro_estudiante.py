from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import relationship
from base import Base

class SeguroME(Base):
    __tablename__ = 'seguro_estudiante'

    # Campos principales
    id_seguro_est = Column(Integer, primary_key=True, autoincrement=True)
    seguro_med_id = Column(Integer, ForeignKey('seguro_medico.id_seguro_med'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id_estudiante'), nullable=False)
    nss = Column(String(15), unique=True, nullable=False)
    estatus = Column(Boolean, default=False)
    clinica = Column(String(15), unique=True, nullable=False)

    # Relacion
    seguro_est = relationship("SeguroM", back_populates="seguro_med")
    estudiantes = relationship("Estudiantes", back_populates="seguro_est")