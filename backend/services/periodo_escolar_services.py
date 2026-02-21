from models.periodo_escolar import PeriodoEscolar
from repository.periodo_escolar_repository import PeriodoEscolarRepository

class PeriodoEscolarServices:

    def __init__(self, repo: PeriodoEscolarRepository):
        self.repo = repo

    # Crear periodo_escolar
    def crear_periodo_escolar(self,data: dict) -> PeriodoEscolarRepository:
        # Regla de negocio: periodo_escolar unico
        #if self.repo.existe_rol(data["alias"]):
        #    raise ValueError("El periodo_escolar ya existe")
        
        periodo_escolar = PeriodoEscolar(
            alias=data["alias"],
            inicio=data["inicio"],
            fin=data["fin"],
            activo=data["activo"]
        )

        return self.repo.crear(periodo_escolar)
    
    # Obtener periodo_escolar por ID
    def obtener_periodo_escolar(self, periodo_id: int) -> PeriodoEscolar:
        periodo_escolar = self.repo.obtener_por_id(periodo_id)
        if not periodo_escolar:
            raise ValueError("Rol no encontrado")
        return periodo_escolar
    
    # Listar roles
    def listar_periodo_escolar(self) -> list[PeriodoEscolar]:
        return self.repo.listar()
    
    # Actualizar periodo_escolar
    def actualizar_periodo_escolar(self, periodo_id: int, data: dict) -> PeriodoEscolar:
        periodo_escolar = self.obtener_periodo_escolar(periodo_id)

        # Actualizar campos permitidos
        for campo, valor in data.items():
            if campo == "alias" or campo == "inicio" or campo == "fin" or campo == "activo":
                valor = self.actualizar_periodo_escolar(valor)
            setattr(periodo_escolar, campo, valor)

        return self.repo.actualizar(periodo_escolar)
    
    # Eliminar periodo_escolar
    def eliminar_periodo_escolar(self, periodo_id: int):
        periodo_escolar = self.obtener_periodo_escolar(periodo_id)
        self.repo.eliminar(periodo_escolar)