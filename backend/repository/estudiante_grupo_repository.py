from sqlalchemy.orm import Session
from models.estudiante_grupo import EstudianteGrupo

class EstudianteGrupoRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear estudiante_grupo
    def crear(self, estudiante_grupo: EstudianteGrupo) -> EstudianteGrupo:
        self.db.add(estudiante_grupo)
        self.db.commit()
        self.db.refresh(estudiante_grupo)
        return estudiante_grupo
    
    # Obtner por ID
    def obtener_por_id(self, est_grupo_id: int) -> EstudianteGrupo | None:
        return (
            self.db.query(EstudianteGrupo)
            .filter(EstudianteGrupo.id_est_grupo == est_grupo_id)
            .first()
        )
    
    # Listar estudiante_grupo
    def listar(self) -> list[EstudianteGrupo]:
        return self.db.query(EstudianteGrupo).all()

    # Actualizar estudiante_grupo
    def actualizar(self, estudiante_grupo: EstudianteGrupo) -> EstudianteGrupo:
        self.db.commit()
        self.db.refresh(estudiante_grupo)
        return estudiante_grupo

    # Eliminar estudiante_grupo
    def eliminar(self, estudiante_grupo: EstudianteGrupo) -> None:
        self.db.delete(estudiante_grupo)
        self.db.commit()