from models.estudiante_grupo import EstudianteGrupo
from repository.estudiante_grupo_repository import EstudianteGrupoRepository

class EstudianteGrupoService:

    def __init__(self, repo: EstudianteGrupoRepository):
        self.repo = repo

    # Asignar estudiante a grupo
    def crear_estudiante_grupo(self, data: dict) -> EstudianteGrupo:
        # Regla de negocio: evitar duplicados activos
        if self.repo.existe_estudiante_grupo(
            data["estudiante_id"],
            data["grupo_id"]
        ):
            raise ValueError("El estudiante ya está asignado a este grupo")

        estudiante_grupo = EstudianteGrupo(
            estudiante_id=data["estudiante_id"],
            grupo_id=data["grupo_id"],
        )

        return self.repo.crear(estudiante_grupo)

    # Obtener asignación por ID
    def obtener_estudiante_grupo(self, est_grupo_id: int) -> EstudianteGrupo:
        estudiante_grupo = self.repo.obtener_por_id(est_grupo_id)
        if not estudiante_grupo:
            raise ValueError("Asignación estudiante–grupo no encontrada")
        return estudiante_grupo

    # Listar historial de asignaciones
    def listar_estudiantes_grupos(self) -> list[EstudianteGrupo]:
        return self.repo.listar()

    # Eliminar asignación (opcional)
    def eliminar_estudiante_grupo(self, est_grupo_id: int):
        estudiante_grupo = self.obtener_estudiante_grupo(est_grupo_id)
        self.repo.eliminar(estudiante_grupo)
