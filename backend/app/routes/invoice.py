from typing import Annotated, List
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, Query, APIRouter

from app.db import get_session
from app.models.invoice import Invoice

router = APIRouter(prefix="/invoices", tags=["invoices"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post('', response_model=Invoice)
def create_invoice(
    invoice: Invoice,
    session: SessionDep
) -> Invoice:
    """
    Crea una nueva factura en la base de datos.

    Este endpoint permite crear una nueva factura con sus detalles.
    """
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice

@router.get('', response_model=List[Invoice])
def get_invoices(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[Invoice]:
    """
    Recupera facturas de la base de datos.

    Este endpoint permite recuperar facturas con paginación usando offset y limit.
    """
    invoices = session.exec(select(Invoice).offset(offset).limit(limit)).all()
    return invoices

@router.get('/{invoice_id}', response_model=Invoice)
def get_invoice(
    invoice_id: int,
    session: SessionDep
) -> Invoice:
    """
    Recupera una factura por su ID.

    Este endpoint permite recuperar una factura específica usando su ID.
    """
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail='Factura no encontrada')
    return invoice

@router.delete('/{invoice_id}', response_model=dict)
def delete_invoice(
    invoice_id: int,
    session: SessionDep
) -> dict:
    """
    Elimina una factura de la base de datos por su ID.

    Este endpoint permite eliminar una factura específica usando su ID.
    """
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail='Factura no encontrada')
    session.delete(invoice)
    session.commit()
    return {"message": "Factura eliminada exitosamente"}