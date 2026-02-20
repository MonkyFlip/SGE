from sqlalchemy.orm import Session
from models.genero import Genero

class GeneroRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear genero
    def crear(self, genero: Genero) -> Genero:
        self.db.add(genero)
        self.db.commit()
        self.db.refresh(genero)
        return genero
    
    # Obtner por ID
    def obtener_por_id(self, genero_id: int) -> Genero | None:
        return (
            self.db.query(Genero)
            .filter(Genero.id_genero == genero_id)
            .first()
        )
    
    # Listar genero
    def listar(self) -> list[Genero]:
        return self.db.query(Genero).all()

    # Actualizar genero
    def actualizar(self, genero: Genero) -> Genero:
        self.db.commit()
        self.db.refresh(genero)
        return genero

    # Eliminar genero
    def eliminar(self, genero: Genero) -> None:
        self.db.delete(genero)
        self.db.commit()