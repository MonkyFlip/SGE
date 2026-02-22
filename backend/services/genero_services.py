from models.genero import Genero
from repository.genero_repository import GeneroRepository

class GeneroService:

    def __init__(self, repo: GeneroRepository):
        self.repo = repo

    # Crear género
    def crear_genero(self, data: dict) -> Genero:
        # Regla de negocio: género único
        if self.repo.existe_genero(data["nombre"]):
            raise ValueError("El género ya existe")

        genero = Genero(
            nombre=data["nombre"]
        )

        return self.repo.crear(genero)
    
    # Obtener género por ID
    def obtener_genero(self, genero_id: int) -> Genero:
        genero = self.repo.obtener_por_id(genero_id)
        if not genero:
            raise ValueError("Género no encontrado")
        return genero
    
    # Listar géneros
    def listar_genero(self) -> list[Genero]:
        return self.repo.listar()

    # Actualizar género
    def actualizar_genero(self, genero_id: int, data: dict) -> Genero:
        genero = self.obtener_genero(genero_id)

        if "nombre" in data:
            nuevo_nombre = data["nombre"]

            if (
                nuevo_nombre != genero.nombre
                and self.repo.existe_genero(nuevo_nombre)
            ):
                raise ValueError("El género ya existe")

            genero.nombre = nuevo_nombre

        return self.repo.actualizar(genero)

    # Eliminar género
    def eliminar_genero(self, genero_id: int):
        genero = self.obtener_genero(genero_id)
        self.repo.eliminar(genero)
