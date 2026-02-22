from models.grupo_tutor import GrupoTutor
from repository.grupo_tutor_repository import GrupoTutorRepository

class GrupoTutorService:

    def __init__(self, repo: GrupoTutorRepository):
        self.repo = repo

    # Crear grupo-tutor
    def crear_grupo_tutor(self, data: dict) -> GrupoTutor:
        # Regla de negocio: un tutor no puede repetirse en el mismo grupo
        if self.repo.existe_grupo_tutor(
            data["grupo_id"],
            data["tutor_id"]
        ):
            raise ValueError("El tutor ya está asignado a este grupo")

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

    # Actualizar grupo-tutor (opcional)
    def actualizar_grupo_tutor(self, grupo_tutor_id: int, data: dict) -> GrupoTutor:
        grupo_tutor = self.obtener_grupo_tutor(grupo_tutor_id)

        # Normalmente NO se actualiza esta relación,
        # pero si decides permitirlo:
        campos_permitidos = {"grupo_id", "tutor_id"}

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(grupo_tutor, campo, valor)

        return self.repo.actualizar(grupo_tutor)

    # Eliminar grupo-tutor
    def eliminar_grupo_tutor(self, grupo_tutor_id: int):
        grupo_tutor = self.obtener_grupo_tutor(grupo_tutor_id)
        self.repo.eliminar(grupo_tutor)
