from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import relationship
from datetime import datetime
from .base import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    # Campos principales
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    rol_id = Column(Integer, ForeignKey('roles.id_rol'), nullable=False)

    # Campos de información personal
    nombre = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email_verified = Column(Boolean, default=False)

    # Campos de auditoría
    email_verified_at = Column(datetime.now(), nullable=True)
    created_at = Column(datetime.now(), nullable=False)
    updated_at = Column(datetime.now(), nullable=False)

    # Relaciones
    rol = relationship("Roles", back_populates="usuario")
    tutores = relationship("Tutores", back_populates="usuario")
    estudiantes = relationship("Estudiantes", back_populates="usuario")