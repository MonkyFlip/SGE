from datetime import datetime
from models.soli_psicopedagogia import SoliPsicopedagogia
from repository.soli_psicopedagogia_repository import SoliPsicopedagogiaRepository

class SoliPsicopedagogiaService:

    def __init__(self, repo: SoliPsicopedagogiaRepository):
        self.repo = repo

    # Crear solicitud
    def crear_solicitud(self, data: dict) -> SoliPsicopedagogia:
        solicitud = SoliPsicopedagogia(
            tutor_id=data["tutor_id"],
            estudiante_id=data["estudiante_id"],
            fecha_soli=data["fecha_soli"],
            fecha_lugar=data["fecha_lugar"],
            tipo_servicio=data["tipo_servicio"],
            quien_canaliza=data["quien_canaliza"],
            motivo=data["motivo"],
            observaciones=data.get("observaciones"),
            estado=data["estado"],
            archivo_pdf=data.get("archivo_pdf"),
        )
        return self.repo.crear(solicitud)
    
    # Obtener solicitud por ID
    def obtener_solicitud(self, solicitud_id: int) -> SoliPsicopedagogia:
        solicitud = self.repo.obtener_por_id(solicitud_id)
        if not solicitud:
            raise ValueError("Solicitud no encontrada")
        return solicitud
    
    # Listar solicitudes
    def listar_solicitudes(self) -> list[SoliPsicopedagogia]:
        return self.repo.listar()
    
    # Actualizar solicitud
    def actualizar_solicitud(self, solicitud_id: int, data: dict) -> SoliPsicopedagogia:
        solicitud = self.obtener_solicitud(solicitud_id)

        # Campos permitidos para actualizar
        campos_permitidos = {
            "fecha_lugar",
            "tipo_servicio",
            "quien_canaliza",
            "motivo",
            "observaciones",
            "estado",
            "archivo_pdf"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(solicitud, campo, valor)

        return self.repo.actualizar(solicitud)

    # Eliminar solicitud
    def eliminar_solicitud(self, solicitud_id: int):
        solicitud = self.obtener_solicitud(solicitud_id)
        self.repo.eliminar(solicitud)
