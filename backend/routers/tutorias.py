from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from repository.tutorias_repository import TutoriasRepository
from services.tutorias_services import TutoriasService
from schemas.tutorias import (
    TutoriaCreateSchema,
    TutoriaUpdateSchema,
    TutoriaResponseSchema
)

router = APIRouter(
    prefix="/tutorias",
    tags=["Tutorías"]
)


def get_service(db: Session = Depends(get_db)) -> TutoriasService:
    repo = TutoriasRepository(db)
    return TutoriasService(repo)


# Crear tutoría
@router.post(
    "/",
    response_model=TutoriaResponseSchema,
    status_code=status.HTTP_201_CREATED
)
def crear_tutoria(
    data: TutoriaCreateSchema,
    service: TutoriasService = Depends(get_service)
):
    try:
        return service.crear_tutoria(data.model_dump())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Obtener tutoría por ID
@router.get(
    "/{tutoria_id}",
    response_model=TutoriaResponseSchema
)
def obtener_tutoria(
    tutoria_id: int,
    service: TutoriasService = Depends(get_service)
):
    try:
        return service.obtener_tutoria(tutoria_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# Listar tutorías
@router.get(
    "/",
    response_model=list[TutoriaResponseSchema]
)
def listar_tutorias(
    service: TutoriasService = Depends(get_service)
):
    return service.listar_tutorias()


# Actualizar tutoría
@router.put(
    "/{tutoria_id}",
    response_model=TutoriaResponseSchema
)
def actualizar_tutoria(
    tutoria_id: int,
    data: TutoriaUpdateSchema,
    service: TutoriasService = Depends(get_service)
):
    try:
        return service.actualizar_tutoria(
            tutoria_id,
            data.model_dump(exclude_unset=True)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Eliminar tutoría (física)
@router.delete(
    "/{tutoria_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_tutoria(
    tutoria_id: int,
    service: TutoriasService = Depends(get_service)
):
    try:
        service.eliminar_tutoria(tutoria_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
