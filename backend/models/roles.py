from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Roles(Base):
    __tablename__ = 'roles'

    # Campos principales
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)

    # Relaciones
    usuario = relationship("Usuarios", back_populates="rol")