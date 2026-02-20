from sqlalchemy.orm import Session
from models.estudiantes import Estudiantes

class EstudianteRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear estudiante
    def crear(self, estudiante: Estudiantes) -> Estudiantes:
        self.db.add(estudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante
    
    # Obtner por ID
    def obtener_por_id(self, estudiante_id: int) -> Estudiantes | None:
        return (
            self.db.query(Estudiantes)
            .filter(Estudiantes.id_estudiante == estudiante_id)
            .first()
        )
    
    # Listar estudiante
    def listar(self) -> list[Estudiantes]:
        return self.db.query(Estudiantes).all()

    # Actualizar estudiante
    def actualizar(self, estudiante: Estudiantes) -> Estudiantes:
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante

    # Eliminar estudiante
    def eliminar(self, estudiante: Estudiantes) -> None:
        self.db.delete(estudiante)
        self.db.commit()