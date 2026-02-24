from models.roles import Roles
from repository.roles_repository import RolesRepository

class RolService:

    def __init__(self, repo: RolesRepository):
        self.repo = repo

    # Crear rol
    def crear_rol(self, data: dict) -> Roles:
        if self.repo.existe_rol(data["nombre"]):
            raise ValueError("El rol ya existe")

        rol = Roles(
            nombre=data["nombre"],
            descripcion=data.get("descripcion")
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

        # Actualizar nombre
        if "nombre" in data:
            nuevo_nombre = data["nombre"]

            if (
                nuevo_nombre != rol.nombre
                and self.repo.existe_rol(nuevo_nombre)
            ):
                raise ValueError("El rol ya existe")

            rol.nombre = nuevo_nombre

        # Actualizar descripción
        if "descripcion" in data:
            rol.descripcion = data["descripcion"]

        return self.repo.actualizar(rol)
    
    # Eliminar rol
    def eliminar_rol(self, rol_id: int):
        rol = self.obtener_rol(rol_id)

        if rol.usuario:
            raise ValueError("No se puede eliminar un rol asignado a usuarios")

        self.repo.eliminar(rol)
