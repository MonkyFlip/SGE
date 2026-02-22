from sqlalchemy.orm import Session
from models.estudiante_grupo import EstudianteGrupo

class EstudianteGrupoRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear asignación
    def crear(self, estudiante_grupo: EstudianteGrupo) -> EstudianteGrupo:
        self.db.add(estudiante_grupo)
        self.db.commit()
        self.db.refresh(estudiante_grupo)
        return estudiante_grupo
    
    # Obtener por ID
    def obtener_por_id(self, est_grupo_id: int) -> EstudianteGrupo | None:
        return (
            self.db.query(EstudianteGrupo)
            .filter(EstudianteGrupo.id_est_grupo == est_grupo_id)
            .first()
        )
    
    # Listar historial completo
    def listar(self) -> list[EstudianteGrupo]:
        return self.db.query(EstudianteGrupo).all()

    # Actualizar asignación
    def actualizar(self, estudiante_grupo: EstudianteGrupo) -> EstudianteGrupo:
        self.db.commit()
        self.db.refresh(estudiante_grupo)
        return estudiante_grupo

    # Verificar si el estudiante ya tiene grupo activo
    def existe_grupo_activo_estudiante(self, estudiante_id: int) -> bool:
        return (
            self.db.query(EstudianteGrupo.id_est_grupo)
            .filter(
                EstudianteGrupo.estudiante_id == estudiante_id,
                EstudianteGrupo.activo == True
            )
            .first()
            is not None
        )

    # Verificar duplicado exacto (histórico)
    def existe_estudiante_grupo(self, estudiante_id: int, grupo_id: int) -> bool:
        return (
            self.db.query(EstudianteGrupo.id_est_grupo)
            .filter(
                EstudianteGrupo.estudiante_id == estudiante_id,
                EstudianteGrupo.grupo_id == grupo_id
            )
            .first()
            is not None
        )
