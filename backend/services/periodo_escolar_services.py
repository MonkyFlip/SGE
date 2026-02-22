from models.periodo_escolar import PeriodoEscolar
from repository.periodo_escolar_repository import PeriodoEscolarRepository

class PeriodoEscolarService:

    def __init__(self, repo: PeriodoEscolarRepository):
        self.repo = repo

    # Crear periodo escolar
    def crear_periodo_escolar(self, data: dict) -> PeriodoEscolar:
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

        campos_permitidos = {
            "alias",
            "inicio",
            "fin",
            "activo"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(periodo_escolar, campo, valor)

        return self.repo.actualizar(periodo_escolar)
    
    # Eliminar periodo escolar
    def eliminar_periodo_escolar(self, periodo_id: int):
        periodo_escolar = self.obtener_periodo_escolar(periodo_id)
        self.repo.eliminar(periodo_escolar)
