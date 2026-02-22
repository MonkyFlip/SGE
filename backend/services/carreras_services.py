from datetime import datetime
from models.carreras import Carreras
from repository.carreras_repository import CarrerasRepository

class CarreraService:

    def __init__(self, repo: CarrerasRepository):
        self.repo = repo

    # Crear usuario
    def crear_carrera(self, data: dict) -> Carreras:
        # Regla de negocio: alias único (pendiente)

        carrera = Carreras(
            periodo_id=data["periodo_id"],
            alias=data["alias"],
            inicio=data["inicio"],
            fin=data["fin"],
            activo=data["activo"],

        )

        return self.repo.crear(carrera)

    # Obtener carrera por ID
    def obtener_carrera(self, carrera_id: int) -> Carreras:
        carrera = self.repo.obtener_por_id(carrera_id)
        if not carrera:
            raise ValueError("Carrera no encontrado")
        return carrera

    # Listar usuarios
    def listar_carrera(self) -> list[Carreras]:
        return self.repo.listar()

    # Actualizar carrera
    def actualizar_carrera(self, carrera_id: int, data: dict) -> Carreras:
        carrera = self.obtener_carrera(carrera_id)

        # Actualizar solo campos permitidos (pendiente)
        # alias, inicio, fin, activo

        return self.repo.actualizar(carrera)

    # Eliminar carrera
    def eliminar_carrera(self, carrera_id: int):
        carrera = self.obtener_carrera(carrera_id)
        self.repo.eliminar(carrera)