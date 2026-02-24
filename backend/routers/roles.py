from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from repository.roles_repository import RolesRepository
from services.roles_services import RolService
from schemas.roles import (
    RolCreateSchema,
    RolUpdateSchema,
    RolResponseSchema
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


# Dependency: Service
def get_service(db: Session = Depends(get_db)) -> RolService:
    repo = RolesRepository(db)
    return RolService(repo)


# Crear rol
@router.post(
    "/",
    response_model=RolResponseSchema,
    status_code=status.HTTP_201_CREATED
)
def crear_rol(
    data: RolCreateSchema,
    service: RolService = Depends(get_service)
):
    try:
        return service.crear_rol(data.model_dump())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Obtener rol por ID
@router.get(
    "/{rol_id}",
    response_model=RolResponseSchema
)
def obtener_rol(
    rol_id: int,
    service: RolService = Depends(get_service)
):
    try:
        return service.obtener_rol(rol_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# Listar roles
@router.get(
    "/",
    response_model=list[RolResponseSchema]
)
def listar_roles(
    service: RolService = Depends(get_service)
):
    return service.listar_roles()


# Actualizar rol
@router.put(
    "/{rol_id}",
    response_model=RolResponseSchema
)
def actualizar_rol(
    rol_id: int,
    data: RolUpdateSchema,
    service: RolService = Depends(get_service)
):
    try:
        return service.actualizar_rol(
            rol_id,
            data.model_dump(exclude_unset=True)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# Eliminar rol
@router.delete(
    "/{rol_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_rol(
    rol_id: int,
    service: RolService = Depends(get_service)
):
    try:
        service.eliminar_rol(rol_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
