from sqlalchemy.orm import Session
from models.seguro_estudiante import SeguroEstudiante

class SeguroEstudianteRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear Seguro-Estudiante
    def crear(self, seguro_estudiante: SeguroEstudiante) -> SeguroEstudiante:
        self.db.add(seguro_estudiante)
        self.db.commit()
        self.db.refresh(seguro_estudiante)
        return seguro_estudiante

    # Obtener por ID
    def obtener_por_id(self, seguro_est_id: int) -> SeguroEstudiante | None:
        return (
            self.db.query(SeguroEstudiante)
            .filter(SeguroEstudiante.id_seguro_est == seguro_est_id)
            .first()
        )

    # Obtener por Estudiante
    def obtener_por_nombre(self, estudiante_seguro: str) -> SeguroEstudiante | None:
        return (
            self.db.query(SeguroEstudiante)
            .filter(SeguroEstudiante.estudiante_id == estudiante_seguro)
            .first()
        )

    # Listar Seguros Medicos
    def listar(self) -> list[SeguroEstudiante]:
        return self.db.query(SeguroEstudiante).all()

    # Actualizar Seguro-Estudiante
    def actualizar(self, seguro_estudiante: SeguroEstudiante) -> SeguroEstudiante:
        self.db.commit()
        self.db.refresh(seguro_estudiante)
        return seguro_estudiante

    # Eliminar Seguro-Estudiante
    def eliminar(self, seguro_estudiante: SeguroEstudiante) -> None:
        self.db.delete(seguro_estudiante)
        self.db.commit()
