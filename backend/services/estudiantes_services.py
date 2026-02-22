from models.estudiantes import Estudiantes
from repository.estudiantes_repository import EstudianteRepository

class EstudianteService:

    def __init__(self, repo: EstudianteRepository):
        self.repo = repo

    # Crear estudiante
    def crear_estudiante(self, data: dict) -> Estudiantes:
        # Regla de negocio: matrícula única
        if self.repo.existe_matricula(data["matricula"]):
            raise ValueError("La matrícula ya está registrada")

        estudiante = Estudiantes(
            usuario_id=data["usuario_id"],
            genero_id=data["genero_id"],
            matricula=data["matricula"],
            telefono=data.get("telefono"),
            activo=data.get("activo", True),
        )

        return self.repo.crear(estudiante)

    # Obtener estudiante por ID
    def obtener_estudiante(self, estudiante_id: int) -> Estudiantes:
        estudiante = self.repo.obtener_por_id(estudiante_id)
        if not estudiante:
            raise ValueError("Estudiante no encontrado")
        return estudiante

    # Listar estudiantes
    def listar_estudiantes(self) -> list[Estudiantes]:
        return self.repo.listar()

    # Actualizar estudiante
    def actualizar_estudiante(self, estudiante_id: int, data: dict) -> Estudiantes:
        estudiante = self.obtener_estudiante(estudiante_id)

        # Campos permitidos para actualizar
        campos_permitidos = {
            "genero_id",
            "telefono",
            "activo"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(estudiante, campo, valor)

        return self.repo.actualizar(estudiante)

    # Eliminar estudiante
    def eliminar_estudiante(self, estudiante_id: int):
        estudiante = self.obtener_estudiante(estudiante_id)
        self.repo.eliminar(estudiante)
