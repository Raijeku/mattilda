from typing import Annotated, List
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, Query, APIRouter

from db import get_session
from models.student import Student

router = APIRouter(prefix="/students", tags=["students"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post('', response_model=Student)
def create_student(
    student: Student,
    session: SessionDep
) -> Student:
    """
    Crea un nuevo estudiante en la base de datos.

    Este endpoint permite crear un nuevo estudiante con sus detalles.
    """
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@router.get('', response_model=List[Student])
def get_students(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[Student]:
    """
    Recupera estudiantes de la base de datos.

    Este endpoint permite recuperar estudiantes con paginación usando offset y limit.
    """
    students = session.exec(select(Student).offset(offset).limit(limit)).all()
    return students

@router.get('/{student_id}', response_model=Student)
def get_student(
    student_id: int,
    session: SessionDep
) -> Student:
    """
    Recupera un estudiante por su ID.

    Este endpoint permite recuperar un estudiante específico usando su ID.
    """
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.delete('/{student_id}', response_model=dict)
def delete_student(
    student_id: int,
    session: SessionDep
) -> dict:
    """
    Elimina un estudiante de la base de datos por su ID.

    Este endpoint permite eliminar un estudiante específico usando su ID.
    """
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    session.delete(student)
    session.commit()