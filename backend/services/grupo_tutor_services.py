from models.grupo_tutor import GrupoTutor
from repository.grupo_tutor_repository import GrupoTutorRepository

class GrupoTutorService:

    def __init__(self, repo: GrupoTutorRepository):
        self.repo = repo

    # Crear grupo_tutor
    def crear_grupo_tutor(self, data: dict) -> GrupoTutor:
        # Regla de negocio: grupo_tutor unico

        grupo_tutor = GrupoTutor(
            grupo_id=data["grupo_id"],
            tutor_id=data["nombre"]
        )

        return self.repo.crear(grupo_tutor)
    
    # Obtener grupo_tutor por ID
    def obtener_grupo_tutor(self, grupo_tutor_id: int) -> GrupoTutor:
        grupo_tutor = self.repo.obtener_por_id(grupo_tutor_id)
        if not grupo_tutor:
            raise ValueError("Grupo no encontrado")
        return grupo_tutor
    
    # Listar grupos
    def listar_grupos_tutor(self) -> list[GrupoTutor]:
        return self.repo.listar()

    # Actualizar grupo_tutor
    def actualizar_grupo_tutor(self, grupo_tutor_id: int, data: dict) -> GrupoTutor:
        grupo_tutor = self.obtener_grupo_tutor(grupo_tutor_id)

        # Actualizar solo campos permitidos

        return self.repo.actualizar(grupo_tutor)

    # Eliminar grupo_tutor
    def eliminar_grupo_tutor(self, grupo_tutor_id: int):
        grupo_tutor = self.obtener_grupo_tutor(grupo_tutor_id)
        self.repo.eliminar(grupo_tutor)