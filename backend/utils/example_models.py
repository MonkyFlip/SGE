from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ============================================================
#  MANY-TO-MANY (M:M)
#  Tabla intermedia para estudiantes y cursos
# ============================================================

estudiante_curso = Table(
    "estudiante_curso",
    Base.metadata,
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"), primary_key=True),
    Column("curso_id", Integer, ForeignKey("cursos.id"), primary_key=True)
)

# ============================================================
#  ONE-TO-ONE (1:1)
#  Persona ↔ Pasaporte
# ============================================================

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    # Relación 1:1
    pasaporte = relationship("Pasaporte", back_populates="persona", uselist=False)


class Pasaporte(Base):
    __tablename__ = "pasaportes"

    id = Column(Integer, primary_key=True)
    numero = Column(String(50), nullable=False)

    persona_id = Column(Integer, ForeignKey("personas.id"), unique=True)

    persona = relationship("Persona", back_populates="pasaporte")

# ============================================================
#  ONE-TO-MANY (1:M)
#  Categoria → Productos
# ============================================================

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    # Relación 1:M
    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="productos")

# ============================================================
#  MANY-TO-MANY (M:M)
#  Estudiantes ↔ Cursos
# ============================================================

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    cursos = relationship(
        "Curso",
        secondary=estudiante_curso,
        back_populates="estudiantes"
    )


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estudiantes = relationship(
        "Estudiante",
        secondary=estudiante_curso,
        back_populates="cursos"
    )
