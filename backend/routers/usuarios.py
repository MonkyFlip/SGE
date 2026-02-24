from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from repository.usuarios_repository import UsuariosRepository
from services.usuarios_services import UsuariosService
from schemas.usuarios import (
    UsuarioCreateSchema,
    UsuarioUpdateSchema,
    UsuarioResponseSchema
)

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


def get_service(db: Session = Depends(get_db)) -> UsuariosService:
    repo = UsuariosRepository(db)
    return UsuariosService(repo)


# Crear usuario
@router.post(
    "/",
    response_model=UsuarioResponseSchema,
    status_code=status.HTTP_201_CREATED
)
def crear_usuario(
    data: UsuarioCreateSchema,
    service: UsuariosService = Depends(get_service)
):
    try:
        return service.crear_usuario(data.model_dump())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Obtener usuario
@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponseSchema
)
def obtener_usuario(
    usuario_id: int,
    service: UsuariosService = Depends(get_service)
):
    try:
        return service.obtener_usuario(usuario_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# Listar usuarios
@router.get(
    "/",
    response_model=list[UsuarioResponseSchema]
)
def listar_usuarios(
    service: UsuariosService = Depends(get_service)
):
    return service.listar_usuarios()


# Actualizar usuario
@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponseSchema
)
def actualizar_usuario(
    usuario_id: int,
    data: UsuarioUpdateSchema,
    service: UsuariosService = Depends(get_service)
):
    try:
        return service.actualizar_usuario(
            usuario_id,
            data.model_dump(exclude_unset=True)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Eliminación lógica
@router.delete(
    "/{usuario_id}",
    response_model=UsuarioResponseSchema
)
def eliminar_usuario(
    usuario_id: int,
    service: UsuariosService = Depends(get_service)
):
    try:
        return service.eliminar_usuario(usuario_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
