from models.roles import Roles
from repository.roles_repository import RolesRepository

class RolServices:

    def __init__(self, repo: RolesRepository):
        self.repo = repo

    # Crear rol
    def crear_rol(self,data: dict) -> RolesRepository:
        # Regla de negocio: rol unico
        if self.repo.existe_rol(data["nombre"]):
            raise ValueError("El rol ya existe")
        
        rol = Roles(
            nombre=data["nombre"],
            descripcion=data["descripcion"]
        )

        return self.repo.crear(rol)
    
    # Obtener rol por ID
    def obtener_rol(self, rol_id: int) -> Roles:
        rol = self.repo.obtener_por_id(rol_id)
        if not rol:
            raise ValueError("Rol no encontrado")
        return rol
    
    # Listar roles
    def listar_roles(self) -> list[Roles]:
        return self.repo.listar()
    
    # Actualizar rol
    def actualizar_rol(self, rol_id: int, data: dict) -> Roles:
        rol = self.obtener_rol(rol_id)

        # Actualizar campos permitidos
        for campo, valor in data.items():
            if campo == "nombre" or campo == "descripcion":
                valor = self.actualizar_rol(valor)
            setattr(rol, campo, valor)

        return self.repo.actualizar(rol)
    
    # Eliminar rol
    def eliminar_rol(self, rol_id: int):
        rol = self.obtener_rol(rol_id)
        self.repo.eliminar(rol)