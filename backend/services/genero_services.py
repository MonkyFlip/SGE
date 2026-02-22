from models.genero import Genero
from repository.genero_repository import GeneroRepository

class GeneroService:

    def __init__(self, repo: GeneroRepository):
        self.repo = repo

    # Crear genero
    def crear_genero(self, data: dict) -> Genero:
        # Regla de negocio: genero unico

        genero = Genero(
            nomre=data["nomre"]
        )

        return self.repo.crear(genero)
    
    # Obtener genero por ID
    def obtener_genero(self, genero_id: int) -> Genero:
        genero = self.repo.obtener_por_id(genero_id)
        if not genero:
            raise ValueError("Genero no encontrado")
        return genero
    
    # Listar grupos
    def listar_genero(self) -> list[Genero]:
        return self.repo.listar()

    # Actualizar genero
    def actualizar_genero(self, genero_id: int, data: dict) -> Genero:
        genero = self.obtener_genero(genero_id)

        # Actualizar solo campos permitidos

        return self.repo.actualizar(genero)

    # Eliminar genero
    def eliminar_genero(self, genero_id: int):
        genero = self.obtener_genero(genero_id)
        self.repo.eliminar(genero)