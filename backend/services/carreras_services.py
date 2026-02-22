from models.carreras import Carreras
from repository.carreras_repository import CarrerasRepository

class CarreraService:

    def __init__(self, repo: CarrerasRepository):
        self.repo = repo

    def crear_carrera(self, data: dict) -> Carreras:
        if self.repo.existe_carrera(data["periodo_id"], data["alias"]):
            raise ValueError("Ya existe una carrera con ese alias en este periodo")

        carrera = Carreras(
            periodo_id=data["periodo_id"],
            alias=data["alias"],
            inicio=data["inicio"],
            fin=data["fin"],
            activo=data.get("activo", True),
        )

        return self.repo.crear(carrera)

    def obtener_carrera(self, carrera_id: int) -> Carreras:
        carrera = self.repo.obtener_por_id(carrera_id)
        if not carrera:
            raise ValueError("Carrera no encontrada")
        return carrera

    def listar_carrera(self) -> list[Carreras]:
        return self.repo.listar()

    def actualizar_carrera(self, carrera_id: int, data: dict) -> Carreras:
        carrera = self.obtener_carrera(carrera_id)

        if "alias" in data:
            nuevo_alias = data["alias"]
            if (
                nuevo_alias != carrera.alias
                and self.repo.existe_carrera(carrera.periodo_id, nuevo_alias)
            ):
                raise ValueError("Ya existe una carrera con ese alias en este periodo")
            carrera.alias = nuevo_alias

        if "inicio" in data:
            carrera.inicio = data["inicio"]

        if "fin" in data:
            carrera.fin = data["fin"]

        if "activo" in data:
            carrera.activo = data["activo"]

        return self.repo.actualizar(carrera)

    # Baja lógica
    def eliminar_carrera(self, carrera_id: int):
        carrera = self.obtener_carrera(carrera_id)
        carrera.activo = False
        return self.repo.actualizar(carrera)
