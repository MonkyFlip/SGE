from models.tutores import Tutores
from repository.tutores_repository import TutoresRepository

class TutoresService:
    
    def __init__(self, repo: TutoresRepository):
        self.repo = repo

    # Crear tutor
    def crear_tutor(self, data: dict) -> Tutores:
        # Regla de negocio: clave_sp única
        if self.repo.existente_clave_sp(data["clave_sp"]):
            raise ValueError("La clave SP ya está registrada")
        
        tutor = Tutores(
            usuario_id=data["usuario_id"],
            clave_sp=data["clave_sp"],
            telefono=data.get("telefono"),
            activo=data.get("activo", True)
        )

        return self.repo.crear(tutor)
    
    # Obtener tutor por ID
    def obtener_tutor(self, tutor_id: int) -> Tutores:
        tutor = self.repo.obtener_por_id(tutor_id)
        if not tutor:
            raise ValueError("Tutor no encontrado")
        return tutor
    
    # Listar tutores
    def listar_tutores(self) -> list[Tutores]:
        return self.repo.listar()
    
    # Actualizar tutor
    def actualizar_tutor(self, tutor_id: int, data: dict) -> Tutores:
        tutor = self.obtener_tutor(tutor_id)

        # Campos permitidos para actualizar
        campos_permitidos = {
            "clave_sp",
            "telefono",
            "activo"
        }

        # Regla de negocio: clave_sp única (si se intenta cambiar)
        if "clave_sp" in data:
            if self.repo.existente_clave_sp(data["clave_sp"]):
                raise ValueError("La clave SP ya está registrada")

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(tutor, campo, valor)

        return self.repo.actualizar(tutor)
    
    # Eliminar tutor
    def eliminar_tutor(self, tutor_id: int):
        tutor = self.obtener_tutor(tutor_id)
        self.repo.eliminar(tutor)
