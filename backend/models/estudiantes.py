from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import relationship
from base import Base

class Estudiantes(Base):
    __tablename__ = 'estudiantes'

    # Campos principales
    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer,ForeignKey('usuarios.id_usuario'), nullable=False)
    genero_id = Column(Integer,ForeignKey('genero.id_genero'), nullable=False)
    matricula = Column(String(30), nullable=False, unique=True)
    telefono = Column(String(15), nullable=False, unique=True)
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuarios", back_populates="estudiantes")
    genero = relationship("Genero", back_populates="estudiantes")
    seguro_med = relationship("SeguroME", back_populates="seguro_est")