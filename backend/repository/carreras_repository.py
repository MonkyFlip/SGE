from sqlalchemy.orm import Session
from models.carreras import Carreras

class CarrerasRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear carrera
    def crear(self, carrera: Carreras) -> Carreras:
        self.db.add(carrera)
        self.db.commit()
        self.db.refresh(carrera)
        return carrera
    
    # Obtner por ID
    def obtener_por_id(self, carrera_id: int) -> Carreras | None:
        return (
            self.db.query(Carreras)
            .filter(Carreras.id_carrera == carrera_id)
            .first()
        )
    
    # Listar carrera
    def listar(self) -> list[Carreras]:
        return self.db.query(Carreras).all()

    # Actualizar carrera
    def actualizar(self, carrera: Carreras) -> Carreras:
        self.db.commit()
        self.db.refresh(carrera)
        return carrera

    # Eliminar carrera
    def eliminar(self, carrera: Carreras) -> None:
        self.db.delete(carrera)
        self.db.commit()