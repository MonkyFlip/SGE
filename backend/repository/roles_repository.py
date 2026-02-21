from sqlalchemy.orm import Session
from models.roles import Roles

class RolesRepository:
    
    def __init__(self, db: Session):
        self.db = db

    # Crear rol
    def crear(self, rol: Roles) -> Roles:
        self.db.add(rol)
        self.db.commit()
        self.db.refresh(rol)
        return rol
    
    # Obtener por ID
    def obtener_por_id(self,rol_id: int) -> Roles:
        return(
        self.db.query(Roles)
        .filter_by(Roles.id_rol == rol_id) # .filter()
        .first()
        )
    
    # Verificar si rol existe
    def existe_rol(self, nombre: str) -> bool:
        return(
            self.db.query(Roles.id_rol)
            .filter(Roles.nombre == nombre)
            .first()
            is not None
        )

    # Listar roles
    def listar(self) -> list[Roles]:
        return self.db.query(Roles).all()
    
    # Actualizar rol
    def actualizar(self, rol: Roles) -> Roles:
        self.db.commit()
        self.db.refresh(rol)
        return rol
    
    # Eliminar rol
    def elimiar(self, rol: Roles) -> Roles:
        self.db.delete(rol)
        self.db.commit()