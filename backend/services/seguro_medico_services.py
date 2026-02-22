from models.seguro_medico import SeguroMedico
from repository.seguro_medico_repository import SeguroMedicoRepository

class SeguroMedicoService:

    def __init__(self, repo: SeguroMedicoRepository):
        self.repo = repo

    # Crear seguro medico
    def crear_seguro(self, data: dict) -> SeguroMedico:
        if self.repo.existente_seguro(data["nombre"]):
            raise ValueError("El seguro médico ya está registrado")

        seguro = SeguroMedico(
            nombre=data["nombre"]
        )
        return self.repo.crear(seguro)
    
    # Obtener seguro por ID
    def obtener_seguro(self, seguro_med_id: int) -> SeguroMedico:
        seguro = self.repo.obtener_por_id(seguro_med_id)
        if not seguro:
            raise ValueError("Seguro médico no encontrado")
        return seguro
    
    # Listar seguros
    def listar_seguros(self) -> list[SeguroMedico]:
        return self.repo.listar()
    
    # Actualizar seguro
    def actualizar_seguro(self, seguro_med_id: int, data: dict) -> SeguroMedico:
        seguro = self.obtener_seguro(seguro_med_id)

        # Solo se permite actualizar el nombre
        if "nombre" in data:
            nuevo_nombre = data["nombre"]

            # Validar unicidad si cambia el nombre
            if (
                nuevo_nombre != seguro.nombre
                and self.repo.existente_seguro(nuevo_nombre)
            ):
                raise ValueError("El seguro médico ya está registrado")

            seguro.nombre = nuevo_nombre

        return self.repo.actualizar(seguro)

    # Eliminar seguro
    def eliminar_seguro(self, seguro_med_id: int) -> None:
        seguro = self.obtener_seguro(seguro_med_id)
        self.repo.eliminar(seguro)
