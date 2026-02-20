from sqlalchemy.orm import Session
from models.tutorias import Tutorias

class TutoriasRepository:

    def __init__(self, db:Session):
        self.db = db

    # Crear Tutoria
    def crear(self, tutoria: Tutorias) -> Tutorias:
        self.db.add(tutoria)
        self.db.commit()
        self.db.refresh(tutoria)
        return tutoria
    
    # Obtener por ID
    def obtener_por_id(self, tutoria_id: int) -> Tutorias | None:
        return(
            self.db.query(Tutorias)
            .filter(Tutorias.id_tutoria == tutoria_id)
            .first()
        )
    
    # Obtener por Tutor
    def obtener_por_tutor(self, tutor_id: int) -> Tutorias | None:
        return(
            self.db.query(Tutorias)
            .filter(Tutorias.tutor_id == tutor_id)
            .first()
        )

    # Obtener por Estudiante
    def obtener_por_estudiante(self, estudiante_id: int) -> Tutorias | None:
        return(
            self.db.query(Tutorias)
            .filter(Tutorias.estudiante_id == estudiante_id)
            .first()
        )
    
    # Listar Tutorias
    def listar(self) -> list[Tutorias]:
        return self.db.query(Tutorias).all()

    # Actualizar Tutoria
    def actualizar(self, tutoria: Tutorias) -> Tutorias:
        self.db.commit()
        self.db.refresh(tutoria)
        return tutoria

    # Eliminar Tutoria
    def eliminar(self, tutoria: Tutorias) -> None:
        self.db.delete(tutoria)
        self.db.commit()
