from models.estudiante_grupo import EstudianteGrupo
from repository.estudiante_grupo_repository import EstudianteGrupoRepository


class EstudianteGrupoService:

    def __init__(self, repo: EstudianteGrupoRepository):
        self.repo = repo

    # Asignar estudiante a grupo
    def crear_estudiante_grupo(self, data: dict) -> EstudianteGrupo:
        # Regla de negocio: un estudiante solo puede tener un grupo activo
        if self.repo.existe_grupo_activo_estudiante(data["estudiante_id"]):
            raise ValueError("El estudiante ya tiene un grupo activo")

        estudiante_grupo = EstudianteGrupo(
            estudiante_id=data["estudiante_id"],
            grupo_id=data["grupo_id"],
            activo=True
        )

        return self.repo.crear(estudiante_grupo)

    # Obtener asignación por ID
    def obtener_estudiante_grupo(self, est_grupo_id: int) -> EstudianteGrupo:
        estudiante_grupo = self.repo.obtener_por_id(est_grupo_id)
        if not estudiante_grupo:
            raise ValueError("Asignación estudiante–grupo no encontrada")
        return estudiante_grupo

    # Listar historial completo de asignaciones
    def listar_estudiantes_grupos(self) -> list[EstudianteGrupo]:
        return self.repo.listar()

    # Cerrar asignación (baja lógica)
    def cerrar_estudiante_grupo(self, est_grupo_id: int) -> EstudianteGrupo:
        estudiante_grupo = self.obtener_estudiante_grupo(est_grupo_id)

        if not estudiante_grupo.activo:
            raise ValueError("La asignación ya está cerrada")

        estudiante_grupo.activo = False
        return self.repo.actualizar(estudiante_grupo)
