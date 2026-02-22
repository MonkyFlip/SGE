from models.periodo_escolar import PeriodoEscolar
from repository.periodo_escolar_repository import PeriodoEscolarRepository


class PeriodoEscolarService:

    def __init__(self, repo: PeriodoEscolarRepository):
        self.repo = repo

    # Crear periodo escolar
    def crear_periodo_escolar(self, data: dict) -> PeriodoEscolar:
        # Regla de negocio: alias único
        if self.repo.existe_alias(data["alias"]):
            raise ValueError("El alias del periodo escolar ya existe")

        # Regla de negocio: solo un periodo activo
        if data.get("activo", False):
            self.repo.desactivar_periodos_activos()

        periodo_escolar = PeriodoEscolar(
            alias=data["alias"],
            inicio=data["inicio"],
            fin=data["fin"],
            activo=data.get("activo", False)
        )

        return self.repo.crear(periodo_escolar)
    
    # Obtener periodo escolar por ID
    def obtener_periodo_escolar(self, periodo_id: int) -> PeriodoEscolar:
        periodo_escolar = self.repo.obtener_por_id(periodo_id)
        if not periodo_escolar:
            raise ValueError("Periodo escolar no encontrado")
        return periodo_escolar
    
    # Listar periodos escolares
    def listar_periodo_escolar(self) -> list[PeriodoEscolar]:
        return self.repo.listar()
    
    # Actualizar periodo escolar
    def actualizar_periodo_escolar(self, periodo_id: int, data: dict) -> PeriodoEscolar:
        periodo_escolar = self.obtener_periodo_escolar(periodo_id)

        # Validar cambio de alias
        if "alias" in data:
            nuevo_alias = data["alias"]
            if (
                nuevo_alias != periodo_escolar.alias
                and self.repo.existe_alias(nuevo_alias)
            ):
                raise ValueError("El alias del periodo escolar ya existe")
            periodo_escolar.alias = nuevo_alias

        # Manejo de periodo activo
        if "activo" in data and data["activo"]:
            self.repo.desactivar_periodos_activos()
            periodo_escolar.activo = True
        elif "activo" in data:
            periodo_escolar.activo = data["activo"]

        # Fechas
        if "inicio" in data:
            periodo_escolar.inicio = data["inicio"]

        if "fin" in data:
            periodo_escolar.fin = data["fin"]

        return self.repo.actualizar(periodo_escolar)
    
    # Eliminar periodo escolar
    def eliminar_periodo_escolar(self, periodo_id: int):
        periodo_escolar = self.obtener_periodo_escolar(periodo_id)
        self.repo.eliminar(periodo_escolar)
