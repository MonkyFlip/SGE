from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Genero(Base):
    __tablename__ = 'genero'

    # Campos principales
    id_genero = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)

    # Relaciones
    estudiantes = relationship("Estudiantes", back_populates="genero")