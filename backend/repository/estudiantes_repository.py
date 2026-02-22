from sqlalchemy.orm import Session
from models.estudiantes import Estudiantes

class EstudianteRepository:

    def __init__(self, db: Session):
        self.db = db

    def crear(self, estudiante: Estudiantes) -> Estudiantes:
        self.db.add(estudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante
    
    def obtener_por_id(self, estudiante_id: int) -> Estudiantes | None:
        return (
            self.db.query(Estudiantes)
            .filter(Estudiantes.id_estudiante == estudiante_id)
            .first()
        )
    
    def listar(self) -> list[Estudiantes]:
        return self.db.query(Estudiantes).all()

    def actualizar(self, estudiante: Estudiantes) -> Estudiantes:
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante
