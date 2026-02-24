from datetime import datetime, timezone
from passlib.context import CryptContext

from models.usuarios import Usuarios
from repository.usuarios_repository import UsuariosRepository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UsuariosService:

    def __init__(self, repo: UsuariosRepository):
        self.repo = repo

    # Crear usuario
    def crear_usuario(self, data: dict) -> Usuarios:
        if self.repo.existe_email(data["email"]):
            raise ValueError("El correo ya está registrado")

        hashed_password = self._hash_password(data["password"])

        usuario = Usuarios(
            rol_id=data["rol_id"],
            nombre=data["nombre"],
            apellido_paterno=data["apellido_paterno"],
            apellido_materno=data["apellido_materno"],
            email=data["email"],
            password=hashed_password,
            email_verified=False,
            created_at=datetime.now(timezone.utc)
        )

        return self.repo.crear(usuario)

    # Obtener usuario
    def obtener_usuario(self, usuario_id: int) -> Usuarios:
        usuario = self.repo.obtener_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        return usuario

    # Listar usuarios
    def listar_usuarios(self) -> list[Usuarios]:
        return self.repo.listar()

    # Actualizar usuario
    def actualizar_usuario(self, usuario_id: int, data: dict) -> Usuarios:
        usuario = self.obtener_usuario(usuario_id)

        campos_permitidos = {
            "rol_id",
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "email",
            "password"
        }

        for campo, valor in data.items():
            if campo not in campos_permitidos:
                continue

            if campo == "password":
                valor = self._hash_password(valor)

            setattr(usuario, campo, valor)

        usuario.updated_at = datetime.now(timezone.utc)
        return self.repo.actualizar(usuario)

    # Eliminación lógica
    def eliminar_usuario(self, usuario_id: int) -> Usuarios:
        usuario = self.obtener_usuario(usuario_id)

        if usuario.estado == "INACTIVO":
            raise ValueError("El usuario ya está inactivo")

        usuario.updated_at = datetime.now(timezone.utc)
        return self.repo.desactivar(usuario)

    # Verificar email
    def verificar_email(self, usuario_id: int) -> Usuarios:
        usuario = self.obtener_usuario(usuario_id)
        usuario.email_verified = True
        usuario.email_verified_at = datetime.now(timezone.utc)
        return self.repo.actualizar(usuario)

    # Utilidad interna
    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
