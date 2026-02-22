from sqlalchemy.orm import Session
from models.grupo_tutor import GrupoTutor

class GrupoTutorRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear grupo_tutor
    def crear(self, grupo_tutor: GrupoTutor) -> GrupoTutor:
        self.db.add(grupo_tutor)
        self.db.commit()
        self.db.refresh(grupo_tutor)
        return grupo_tutor
    
    # Obtner por ID
    def obtener_por_id(self, grupo_tutor_id: int) -> GrupoTutor | None:
        return (
            self.db.query(GrupoTutor)
            .filter(GrupoTutor.id_grupo_tutor == grupo_tutor_id)
            .first()
        )
    
    # Listar grupo_tutor
    def listar(self) -> list[GrupoTutor]:
        return self.db.query(GrupoTutor).all()

    # Actualizar grupo_tutor
    def actualizar(self, grupo_tutor: GrupoTutor) -> GrupoTutor:
        self.db.commit()
        self.db.refresh(grupo_tutor)
        return grupo_tutor

    # Eliminar grupo_tutor
    def eliminar(self, grupo_tutor: GrupoTutor) -> None:
        self.db.delete(grupo_tutor)
        self.db.commit()

    def existe_tutor_en_grupo(self, grupo_id: int) -> bool:
        return (
            self.db.query(GrupoTutor.id_grupo_tutor)
            .filter(GrupoTutor.grupo_id == grupo_id)
            .first()
            is not None
        )
