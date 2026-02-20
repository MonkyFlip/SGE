from sqlalchemy.orm import Session
from models.usuarios import Usuarios

class UsuariosRepository:

    def __init__(self, db: Session):
        self.db = db

    # Crear usuario
    def crear(self, usuario: Usuarios) -> Usuarios:
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # Obtener por ID
    def obtener_por_id(self, usuario_id: int) -> Usuarios | None:
        return (
            self.db.query(Usuarios)
            .filter(Usuarios.id_usuario == usuario_id)
            .first()
        )

    # Obtener por email
    def obtener_por_email(self, email: str) -> Usuarios | None:
        return (
            self.db.query(Usuarios)
            .filter(Usuarios.email == email)
            .first()
        )

    # Verificar si email existe
    def existe_email(self, email: str) -> bool:
        return (
            self.db.query(Usuarios.id_usuario)
            .filter(Usuarios.email == email)
            .first()
            is not None
        )

    # Listar usuarios
    def listar(self) -> list[Usuarios]:
        return self.db.query(Usuarios).all()

    # Actualizar usuario
    def actualizar(self, usuario: Usuarios) -> Usuarios:
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # Eliminar usuario
    def eliminar(self, usuario: Usuarios) -> None:
        self.db.delete(usuario)
        self.db.commit()
