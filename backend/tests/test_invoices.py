from fastapi.testclient import TestClient
from sqlmodel import delete
from app.main import app
from app.db import get_session
from app.models.invoice import Invoice
from app.models.student import Student
from app.models.school import School
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    session = next(get_session())
    session.exec(delete(Invoice))
    session.exec(delete(Student))
    session.exec(delete(School))
    session.commit()
    session.close()

def test_create_invoice():
    # Create school
    school_resp = client.post("/schools/", json={"name": "Test School for Invoice"})
    assert school_resp.status_code == 200
    school_id = school_resp.json()["id"]

    # Create student
    student_resp = client.post("/students/", json={"name": "Test Student", "school_id": school_id})
    assert student_resp.status_code == 200
    student_id = student_resp.json()["id"]

    # Create invoice
    invoice_resp = client.post("/invoices/", json={
        "amount": 150.0,
        "description": "Test Invoice",
        "student_id": student_id,
        "school_id": school_id
    })
    assert invoice_resp.status_code == 200
    data = invoice_resp.json()
    assert data["amount"] == 150.0
    assert data["description"] == "Test Invoice"

def test_get_invoices():
    resp = client.get("/invoices/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_invoice():
    # Create school and student
    school_resp = client.post("/schools/", json={"name": "Test School for Invoice"})
    school_id = school_resp.json()["id"]
    student_resp = client.post("/students/", json={"name": "Test Student", "school_id": school_id})
    student_id = student_resp.json()["id"]

    # Create invoice
    invoice_resp = client.post("/invoices/", json={
        "amount": 200.0,
        "description": "Another Test Invoice",
        "student_id": student_id,
        "school_id": school_id
    })
    invoice_id = invoice_resp.json()["id"]

    # Retrieve invoice
    get_resp = client.get(f"/invoices/{invoice_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == invoice_id
    assert data["amount"] == 200.0
    assert data["description"] == "Another Test Invoice"

def test_delete_invoice():
    # Create school and student
    school_resp = client.post("/schools/", json={"name": "Test School for Invoice"})
    school_id = school_resp.json()["id"]
    student_resp = client.post("/students/", json={"name": "Test Student", "school_id": school_id})
    student_id = student_resp.json()["id"]

    # Create invoice
    invoice_resp = client.post("/invoices/", json={
        "amount": 250.0,
        "description": "Invoice to Delete",
        "student_id": student_id,
        "school_id": school_id
    })
    invoice_id = invoice_resp.json()["id"]

    # Delete invoice
    del_resp = client.delete(f"/invoices/{invoice_id}")
    assert del_resp.status_code == 200
    assert del_resp.json() == {"message": "Factura eliminada exitosamente"}