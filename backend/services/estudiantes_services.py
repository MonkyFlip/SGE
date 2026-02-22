from models.estudiantes import Estudiantes
from repository.estudiantes_repository import EstudianteRepository

class EstudianteService:

    def __init__(self, repo: EstudianteRepository):
        self.repo = repo

    def crear_estudiante(self, data: dict) -> Estudiantes:
        if self.repo.existe_matricula(data["matricula"]):
            raise ValueError("La matrícula ya está registrada")

        estudiante = Estudiantes(
            usuario_id=data["usuario_id"],
            genero_id=data["genero_id"],
            matricula=data["matricula"],
            telefono=data.get("telefono"),
            estado="ACTIVO"
        )

        return self.repo.crear(estudiante)

    def obtener_estudiante(self, estudiante_id: int) -> Estudiantes:
        estudiante = self.repo.obtener_por_id(estudiante_id)
        if not estudiante:
            raise ValueError("Estudiante no encontrado")
        return estudiante

    def listar_estudiantes(self) -> list[Estudiantes]:
        return self.repo.listar()

    def actualizar_estudiante(self, estudiante_id: int, data: dict) -> Estudiantes:
        estudiante = self.obtener_estudiante(estudiante_id)

        campos_permitidos = {
            "genero_id",
            "telefono",
            "estado"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(estudiante, campo, valor)

        return self.repo.actualizar(estudiante)

    # Baja lógica
    def dar_baja_estudiante(self, estudiante_id: int) -> Estudiantes:
        estudiante = self.obtener_estudiante(estudiante_id)
        estudiante.estado = "BAJA"
        return self.repo.actualizar(estudiante)
