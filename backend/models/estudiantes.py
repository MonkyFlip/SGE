from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudiantes(Base):
    __tablename__ = 'estudiantes'

    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    genero_id = Column(Integer, ForeignKey('genero.id_genero'), nullable=False)
    matricula = Column(String(30), nullable=False, unique=True)
    telefono = Column(String(15), nullable=False, unique=True)

    # Estado académico
    estado = Column(String(20), nullable=False, default="ACTIVO")

    # Relaciones
    usuario = relationship("Usuarios", back_populates="estudiantes")
    genero = relationship("Genero", back_populates="estudiantes")
    seguro_med = relationship("SeguroMedico", back_populates="seguro_est")
    estudiante_grupo = relationship("EstudianteGrupo", back_populates="estudiantes")
    tutorias = relationship("Tutorias", back_populates="estudiante")
    soli_psicopedagogia = relationship("SoliPsicopedagogia", back_populates="estudiante")
