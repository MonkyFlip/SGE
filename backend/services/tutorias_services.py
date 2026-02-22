from datetime import datetime
from models.tutorias import Tutorias
from repository.tutorias_repository import TutoriasRepository

class TutoriasService:

    def __init__(self, repo: TutoriasRepository):
        self.repo = repo

    # Crear tutoría
    def crear_tutoria(self, data: dict) -> Tutorias:
        tutoria = Tutorias(
            tutor_id=data["tutor_id"],
            estudiante_id=data["estudiante_id"],
            fecha=data["fecha"],
            canalizado=data.get("canalizado", False),
            descripcion=data.get("descripcion"),
            acciones=data.get("acciones"),
            tipo=data["tipo"]
        )
        return self.repo.crear(tutoria)

    # Obtener tutoría por ID
    def obtener_tutoria(self, tutoria_id: int) -> Tutorias:
        tutoria = self.repo.obtener_por_id(tutoria_id)
        if not tutoria:
            raise ValueError("Tutoría no encontrada")
        return tutoria

    # Listar tutorías
    def listar_tutorias(self) -> list[Tutorias]:
        return self.repo.listar()

    # Actualizar tutoría
    def actualizar_tutoria(self, tutoria_id: int, data: dict) -> Tutorias:
        tutoria = self.obtener_tutoria(tutoria_id)

        # Campos permitidos para actualizar
        campos_permitidos = {
            "fecha",
            "canalizado",
            "descripcion",
            "acciones",
            "tipo"
        }

        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(tutoria, campo, valor)

        # Si quieres manejar updated_at:
        tutoria.updated_at = datetime.utcnow()

        return self.repo.actualizar(tutoria)

    # Eliminar tutoría
    def eliminar_tutoria(self, tutoria_id: int) -> None:
        tutoria = self.obtener_tutoria(tutoria_id)
        self.repo.eliminar(tutoria)
