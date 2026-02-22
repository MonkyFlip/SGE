from models.estudiante_grupo import EstudianteGrupo
from repository.estudiante_grupo_repository import EstudianteGrupoRepository

class EstudianteGrupoService:

    def __init__(self, repo: EstudianteGrupoRepository):
        self.repo = repo

    # Crear estudiante
    def crear_estudiante_grupo(self, data: dict) -> EstudianteGrupo:

        estudiante_grupo = EstudianteGrupo(
            estudiante_id=data["estudiante_id"],
            grupo_id=data["grupo_id"],
        )

        return self.repo.crear(estudiante_grupo)

    # Obtener estudiante_grupo por ID
    def obtener_estudiante_grupo(self, est_grupo_id: int) -> EstudianteGrupo:
        estudiante_grupo = self.repo.obtener_por_id(est_grupo_id)
        if not estudiante_grupo:
            raise ValueError("studiante no encontrado")
        return estudiante_grupo

    # Listar estudiantes
    def listar_estudiantes_grupos(self) -> list[EstudianteGrupo]:
        return self.repo.listar()

    # Actualizar estudiante
    def actualizar_estudiante_grupo(self, est_grupo_id: int, data: dict) -> EstudianteGrupo:
        estudiante_grupo = self.obtener_estudiante_grupo(est_grupo_id)

        return self.repo.actualizar(estudiante_grupo)

    # Eliminar estudiante
    def eliminar_estudiante_grupo(self, est_grupo_id: int):
        estudiante_grupo = self.obtener_estudiante_grupo(est_grupo_id)
        self.repo.eliminar(estudiante_grupo)

