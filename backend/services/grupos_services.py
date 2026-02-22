from models.grupos import Grupos
from repository.grupos_repository import GruposRepository

class GrupoService:

    def __init__(self, repo: GruposRepository):
        self.repo = repo

    # Crear grupo
    def crear_grupo(self, data: dict) -> Grupos:
        grupo = Grupos(
            carrera_id=data["carrera_id"],
            nombre=data["nombre"],
            activo=data.get("activo", True),
        )
        return self.repo.crear(grupo)
    
    # Obtener grupo por ID
    def obtener_grupo(self, grupo_id: int) -> Grupos:
        grupo = self.repo.obtener_por_id(grupo_id)
        if not grupo:
            raise ValueError("Grupo no encontrado")
        return grupo
    
    # Listar grupos
    def listar_grupos(self) -> list[Grupos]:
        return self.repo.listar()

    # Actualizar grupo
    def actualizar_grupo(self, grupo_id: int, data: dict) -> Grupos:
        grupo = self.obtener_grupo(grupo_id)

        # Campos permitidos para actualizar
        campos_permitidos = {
            "nombre",
            "activo"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(grupo, campo, valor)

        return self.repo.actualizar(grupo)

    # Eliminar grupo
    def eliminar_grupo(self, grupo_id: int):
        grupo = self.obtener_grupo(grupo_id)
        self.repo.eliminar(grupo)
