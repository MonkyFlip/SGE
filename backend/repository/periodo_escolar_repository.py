from sqlalchemy.orm import Session
from models.periodo_escolar import PeriodoEscolar

class PeriodoEscolarRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear periodo
    def crear(self, periodo: PeriodoEscolar) -> PeriodoEscolar:
        self.db.add(periodo)
        self.db.commit()
        self.db.refresh(periodo)
        return periodo
    
    # Obtner por ID
    def obtener_por_id(self, peirodo_id: int) -> PeriodoEscolar | None:
        return (
            self.db.query(PeriodoEscolar)
            .filter(PeriodoEscolar.id_periodo == peirodo_id)
            .first()
        )
    
    # Listar periodos
    def listar(self) -> list[PeriodoEscolar]:
        return self.db.query(PeriodoEscolar).all()

    # Actualizar periodo
    def actualizar(self, periodo: PeriodoEscolar) -> PeriodoEscolar:
        self.db.commit()
        self.db.refresh(periodo)
        return periodo

    # Eliminar periodo
    def eliminar(self, periodo: PeriodoEscolar) -> None:
        self.db.delete(periodo)
        self.db.commit()

    def existe_alias(self, alias: str) -> bool:
        return (
            self.db.query(PeriodoEscolar.id_periodo)
            .filter(PeriodoEscolar.alias == alias)
            .first()
            is not None
        )

    def desactivar_periodos_activos(self):
        self.db.query(PeriodoEscolar).filter(
            PeriodoEscolar.activo == True
        ).update({"activo": False})
        self.db.commit()
