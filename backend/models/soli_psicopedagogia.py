from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

class SoliPsicopedagogia(Base):
    __tablename__ = 'soli_psicopedagogia'

    # Campos principales
    id_solicitud = Column(Integer, primary_key=True, autoincrement=True)
    tutor_id = Column(Integer, ForeignKey('tutores.id_tutor'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id_estudiante'), nullable=False)

    fecha_soli = Column(DateTime(timezone=True), nullable=False,default=lambda: datetime.now(timezone.utc))
    fecha_lugar = Column(String(100), nullable=False)
    tipo_servicio = Column(String(50), nullable=False)
    quien_canaliza = Column(String(100), nullable=False)
    motivo = Column(String(255), nullable=False)
    observaciones = Column(String(255), nullable=True)
    estado = Column(String(20), default="Pendiente")
    archivo_pdf = Column(String(255), nullable=True)

    # Relaciones
    tutor = relationship("Tutores", back_populates="soli_psicopedagogia")
    estudiante = relationship("Estudiantes", back_populates="soli_psicopedagogia")