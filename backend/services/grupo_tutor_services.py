from models.grupo_tutor import GrupoTutor
from repository.grupo_tutor_repository import GrupoTutorRepository


class GrupoTutorService:

    def __init__(self, repo: GrupoTutorRepository):
        self.repo = repo

    # Crear grupo-tutor
    def crear_grupo_tutor(self, data: dict) -> GrupoTutor:
        # Regla de negocio: un grupo solo puede tener un tutor activo
        if self.repo.existe_tutor_en_grupo(data["grupo_id"]):
            raise ValueError("El grupo ya tiene un tutor asignado")

        grupo_tutor = GrupoTutor(
            grupo_id=data["grupo_id"],
            tutor_id=data["tutor_id"]
        )

        return self.repo.crear(grupo_tutor)
    
    # Obtener grupo-tutor por ID
    def obtener_grupo_tutor(self, grupo_tutor_id: int) -> GrupoTutor:
        grupo_tutor = self.repo.obtener_por_id(grupo_tutor_id)
        if not grupo_tutor:
            raise ValueError("Grupo–Tutor no encontrado")
        return grupo_tutor
    
    # Listar grupos-tutor
    def listar_grupos_tutor(self) -> list[GrupoTutor]:
        return self.repo.listar()

    # Eliminar grupo-tutor (desasignar tutor)
    def eliminar_grupo_tutor(self, grupo_tutor_id: int):
        grupo_tutor = self.obtener_grupo_tutor(grupo_tutor_id)
        self.repo.eliminar(grupo_tutor)
