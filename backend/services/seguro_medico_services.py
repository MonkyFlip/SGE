from models.seguro_medico import SeguroMedico
from repository.seguro_medico_repository import SeguroMedicoRepository

class SeguroMedicoService:

    def __init__(self, repo: SeguroMedicoRepository):
        self.repo = repo

    # Crear seguro medico
    def crear_seguro(self, data: dict) -> SeguroMedico:
        # Regla de negocio: seguro único
        if self.repo.existente_seguro(data["nombre"]):
            raise ValueError("El seguro medico ya está registrado")
        
        seguro = SeguroMedico(
            nombre=data["nombre"]
        )

        return self.repo.crear(seguro)
    
    # Obtner seguro por ID
    def obtener_seguro(self, seguro_med_id: int) -> SeguroMedico:
        seguro = self.repo.obtener_por_id(seguro_med_id)
        if not seguro:
            raise ValueError("Seguro Medico no encontrado")
        return seguro
    
    # Listar seguros
    def listar_seguros(self) -> list[SeguroMedico]:
        return self.repo.listar()
    
    # Actualizar seguro
    def actualizar_seguro(self, seguro_med_id: int, data: dict) -> SeguroMedico:
        seguro = self.obtener_seguro(seguro_med_id)

        # Actualizar campo nombre
        for campo, valor in data.items():
            if campo == "nombre":
                valor = self.actualizar_seguro(valor)
            setattr(seguro, campo, valor)

            return self.repo.actualizar(seguro)

    # Eliminar seguro
    def eliminar_seguro(self, seguro_med_id: int) -> SeguroMedico:
        seguro = self.obtener_seguro(seguro_med_id)
        return self.repo.eliminar(seguro)
