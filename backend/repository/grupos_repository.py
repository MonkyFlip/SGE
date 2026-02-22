from sqlalchemy.orm import Session
from models.grupos import Grupos

class GruposRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear grupos
    def crear(self, grupos: Grupos) -> Grupos:
        self.db.add(grupos)
        self.db.commit()
        self.db.refresh(grupos)
        return grupos
    
    # Obtner por ID
    def obtener_por_id(self, grupo_id: int) -> Grupos | None:
        return (
            self.db.query(Grupos)
            .filter(Grupos.id_grupo == grupo_id)
            .first()
        )
    
    # Listar grupos
    def listar(self) -> list[Grupos]:
        return self.db.query(Grupos).all()

    # Actualizar grupos
    def actualizar(self, grupos: Grupos) -> Grupos:
        self.db.commit()
        self.db.refresh(grupos)
        return grupos

    # Eliminar grupos
    def eliminar(self, grupos: Grupos) -> None:
        self.db.delete(grupos)
        self.db.commit()

    def existe_grupo(self, carrera_id: int, nombre: str) -> bool:
        return (
            self.db.query(Grupos.id_grupo)
            .filter(
                Grupos.carrera_id == carrera_id,
                Grupos.nombre == nombre
            )
            .first()
            is not None
        )
