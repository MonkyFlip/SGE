from sqlalchemy.orm import Session
from models.soli_psicopedagogia import SoliPsicopedagogia

class SoliPsicopedagogiaRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear soli_psicopedagogia
    def crear(self, soli_psicopedagogia: SoliPsicopedagogia) -> SoliPsicopedagogia:
        self.db.add(soli_psicopedagogia)
        self.db.commit()
        self.db.refresh(soli_psicopedagogia)
        return soli_psicopedagogia
    
    # Obtner por ID
    def obtener_por_id(self, solicitud_id: int) -> SoliPsicopedagogia | None:
        return (
            self.db.query(SoliPsicopedagogia)
            .filter(SoliPsicopedagogia.id_solicitud == solicitud_id)
            .first()
        )
    
    # Listar soli_psicopedagogia
    def listar(self) -> list[SoliPsicopedagogia]:
        return self.db.query(SoliPsicopedagogia).all()

    # Actualizar soli_psicopedagogia
    def actualizar(self, soli_psicopedagogia: SoliPsicopedagogia) -> SoliPsicopedagogia:
        self.db.commit()
        self.db.refresh(soli_psicopedagogia)
        return soli_psicopedagogia

    # Eliminar soli_psicopedagogia
    def eliminar(self, soli_psicopedagogia: SoliPsicopedagogia) -> None:
        self.db.delete(soli_psicopedagogia)
        self.db.commit()