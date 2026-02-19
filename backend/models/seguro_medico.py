from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import relationship
from base import Base

class SeguroM(Base):
    __tablename__ = 'seguro_medico'

    # Campos principales
    id_seguro_med = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)

    # Relacion
    seguro_med = relationship("SeguroME", back_populates="seguro_est")