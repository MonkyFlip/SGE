from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class SeguroMedico(Base):
    __tablename__ = 'seguro_medico'

    # Campos principales
    id_seguro_med = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)

    # Relacion
    seguro_med = relationship("SeguroEstudiante", back_populates="seguro_med")