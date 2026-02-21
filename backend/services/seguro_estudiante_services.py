from models.seguro_estudiante import SeguroEstudiante
from repository.seguro_estudiante_repository import SeguroEstudianteRepository

class SeguroMedicoService:

    def __init__(self, repo: SeguroEstudianteRepository):
        self.repo = repo

    # Asignar seguro medico a estudiante
    def asignar_seguro(self, data: dict) -> SeguroEstudiante:
        # Regla de negocio: seguro unico de estudiante (pendiente)

        seguro_estudiante = SeguroEstudiante(
            seguro_med_id=data["seguro_med_id"],
            estudiante_id=data["estudiante_id"],
            nss=data["nss"],
            estatus=data["estatus"],
            clinica=data["clinica"],
        )

        return self.repo.crear(seguro_estudiante)
    
    # Obtener seguro_estudiante por ID
    def obtener_seguro_estudiante(self, seguro_est_id: int) -> SeguroEstudiante:
        seguro_estudiante = self.repo.obtener_por_id(seguro_est_id)
        if not seguro_estudiante:
            raise ValueError("Seguro-Estudiante no encontrado")
        return seguro_estudiante
    
    # Listar seguro_estdiante
    def listar_seguro_estudiante(self) -> list[SeguroEstudiante]:
        return self.repo.listar()
    
    # Actualizar seguro_estudiante
    def actualizar_seguro_estudiante(self, seguro_est_id: int, data:dict) -> SeguroEstudiante:
        seguro_estudiante = self.obtener_seguro_estudiante(seguro_est_id)

        # Actualizar campos permitidos
        for campo, valor in data.items():
            if campo == "nss" or campo == "estatus" or campo == "clinica":
                valor = self.actualizar_seguro_estudiante(valor)
            setattr(seguro_estudiante, campo, valor)

        return self.repo.actualizar(seguro_estudiante)
    
    # Eliminar seguro_estudiante
    def eliminar_seguro_estudiante(self, seguro_est_id: int):
        seguro_estudiante = self.obtener_seguro_estudiante(seguro_est_id)
        self.repo.eliminar(seguro_estudiante)
