from sqlalchemy.orm import Session
from models.seguro_medico import SeguroMedico

class SeguroMedicoRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear Seguro Medico
    def crear(self, seguro_medico: SeguroMedico) -> SeguroMedico:
        self.db.add(seguro_medico)
        self.db.commit()
        self.db.refresh(seguro_medico)
        return seguro_medico

    # Obtener por ID
    def obtener_por_id(self, seguro_id: int) -> SeguroMedico | None:
        return (
            self.db.query(SeguroMedico)
            .filter(SeguroMedico.id_seguro_med == seguro_id)
            .first()
        )

    # Obtener por nombre
    def obtener_po_nombre(self, nombre_seguro: str) -> SeguroMedico | None:
        return (
            self.db.query(SeguroMedico)
            .filter(SeguroMedico.nombre == nombre_seguro)
            .first()
        )

    # Listar Seguros Medicos
    def listar(self) -> list[SeguroMedico]:
        return self.db.query(SeguroMedico).all()

    # Actualizar Seguros Medicos
    def actualizar(self, seguro_medico: SeguroMedico) -> SeguroMedico:
        self.db.commit()
        self.db.refresh(seguro_medico)
        return seguro_medico

    # Eliminar Seguro Medico
    def eliminar(self, seguro_medico: SeguroMedico) -> None:
        self.db.delete(seguro_medico)
        self.db.commit()
