from sqlalchemy.orm import Session
from models.tutores import Tutores

class TutoresRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear Tutor
    def crear(self, tutor: Tutores) -> Tutores:
        self.db.add(tutor)
        self.db.commit()
        self.db.refresh(tutor)
        return tutor

    # Obtener por ID
    def obtener_por_id(self, tutor_id: int) -> Tutores | None:
        return (
            self.db.query(Tutores)
            .filter(Tutores.id_tutor == tutor_id)
            .first()
        )

    # Listar Tutores
    def listar(self) -> list[Tutores]:
        return self.db.query(Tutores).all()

    # Actualizar Tutor
    def actualizar(self, tutor: Tutores) -> Tutores:
        self.db.commit()
        self.db.refresh(tutor)
        return tutor

    # Eliminar Tutor
    def eliminar(self, tutor: Tutores) -> None:
        self.db.delete(tutor)
        self.db.commit()
