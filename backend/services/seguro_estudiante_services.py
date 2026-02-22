from models.seguro_estudiante import SeguroEstudiante
from repository.seguro_estudiante_repository import SeguroEstudianteRepository

class SeguroEstudianteService:

    def __init__(self, repo: SeguroEstudianteRepository):
        self.repo = repo

    # Asignar seguro médico a estudiante
    def asignar_seguro(self, data: dict) -> SeguroEstudiante:
        # Regla de negocio: un solo seguro por estudiante
        if self.repo.existe_seguro_estudiante(data["estudiante_id"]):
            raise ValueError("El estudiante ya tiene un seguro asignado")

        seguro_estudiante = SeguroEstudiante(
            seguro_med_id=data["seguro_med_id"],
            estudiante_id=data["estudiante_id"],
            nss=data["nss"],
            estatus=data["estatus"],
            clinica=data["clinica"],
        )

        return self.repo.crear(seguro_estudiante)
    
    # Obtener seguro-estudiante por ID
    def obtener_seguro_estudiante(self, seguro_est_id: int) -> SeguroEstudiante:
        seguro_estudiante = self.repo.obtener_por_id(seguro_est_id)
        if not seguro_estudiante:
            raise ValueError("Seguro–Estudiante no encontrado")
        return seguro_estudiante
    
    # Listar seguros-estudiante
    def listar_seguro_estudiante(self) -> list[SeguroEstudiante]:
        return self.repo.listar()
    
    # Actualizar seguro-estudiante
    def actualizar_seguro_estudiante(self, seguro_est_id: int, data: dict) -> SeguroEstudiante:
        seguro_estudiante = self.obtener_seguro_estudiante(seguro_est_id)

        # Campos permitidos
        campos_permitidos = {
            "nss",
            "estatus",
            "clinica"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(seguro_estudiante, campo, valor)

        return self.repo.actualizar(seguro_estudiante)
    
    # Eliminar seguro-estudiante
    def eliminar_seguro_estudiante(self, seguro_est_id: int):
        seguro_estudiante = self.obtener_seguro_estudiante(seguro_est_id)
        self.repo.eliminar(seguro_estudiante)
