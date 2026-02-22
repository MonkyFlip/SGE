from sqlalchemy.orm import Session
from models.carreras import Carreras

class CarrerasRepository:

    def __init__(self, db: Session):
        self.db = db

    def crear(self, carrera: Carreras) -> Carreras:
        self.db.add(carrera)
        self.db.commit()
        self.db.refresh(carrera)
        return carrera
    
    def obtener_por_id(self, carrera_id: int) -> Carreras | None:
        return (
            self.db.query(Carreras)
            .filter(Carreras.id_carrera == carrera_id)
            .first()
        )
    
    # Alias único por periodo
    def existe_carrera(self, periodo_id: int, alias: str) -> bool:
        return (
            self.db.query(Carreras.id_carrera)
            .filter(
                Carreras.periodo_id == periodo_id,
                Carreras.alias == alias
            )
            .first()
            is not None
        )

    def listar(self) -> list[Carreras]:
        return self.db.query(Carreras).all()

    def actualizar(self, carrera: Carreras) -> Carreras:
        self.db.commit()
        self.db.refresh(carrera)
        return carrera
