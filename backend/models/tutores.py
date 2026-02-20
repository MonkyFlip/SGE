from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tutores(Base):
    __tablename__ = 'tutores'

    # Campos principales
    id_tutor = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    clave_sp = Column(Integer, nullable=False, unique=True)
    telefono = Column(String(15), nullable=True, unique=True)
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuarios", back_populates="tutores")
    grupo_tutor = relationship("GrupoTutor", back_populates="tutores")
    tutorias = relationship("Tutorias", back_populates="tutor")
    soli_psicopedagogia = relationship("SoliPsicopedagogia", back_populates="tutor")