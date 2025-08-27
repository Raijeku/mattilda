from typing import Annotated, List
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, Query, APIRouter

from db import get_session
from models.school import School

router = APIRouter(prefix="/schools", tags=["schools"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post('', response_model=School)
def create_school(
    school: School,
    session: SessionDep
) -> School:
    """
    Crea una nueva escuela en la base de datos.

    Este endpoint permite crear una nueva escuela con sus detalles.
    """
    session.add(school)
    session.commit()
    session.refresh(school)
    return school

@router.get('', response_model=List[School])
def get_schools(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[School]:
    """
    Recupera escuelas de la base de datos.

    Este endpoint permite recuperar escuelas con paginación usando offset y limit.
    """
    schools = session.exec(select(School).offset(offset).limit(limit)).all()
    return schools

@router.get('/{school_id}', response_model=School)
def get_school(
    school_id: int,
    session: SessionDep
) -> School:
    """
    Recupera una escuela por su ID.

    Este endpoint permite recuperar una escuela específica usando su ID.
    """
    school = session.get(School, school_id)
    if not school:
        raise HTTPException(status_code=404, detail='School not found')
    return school

@router.delete('/{school_id}', response_model=dict)
def delete_school(
    school_id: int,
    session: SessionDep
) -> dict:
    """
    Elimina una escuela de la base de datos por su ID.

    Este endpoint permite eliminar una escuela específica usando su ID.
    """
    school = session.get(School, school_id)
    if not school:
        raise HTTPException(status_code=404, detail='School not found')
    session.delete(school)
    session.commit()
    return {'success': True}