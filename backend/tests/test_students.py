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

def test_create_student():
    school_resp = client.post("/schools/", json={"name": "Test School for Student"})
    assert school_resp.status_code == 200
    school_id = school_resp.json()["id"]

    student_resp = client.post("/students/", json={"name": "John", "school_id": school_id})
    assert student_resp.status_code == 200
    data = student_resp.json()
    assert data["name"] == "John"

def test_get_students():
    resp = client.get("/students/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_student():
    school_resp = client.post("/schools/", json={"name": "Test School for Student Retrieval"})
    school_id = school_resp.json()["id"]

    student_resp = client.post("/students/", json={"name": "Jane", "school_id": school_id})
    student_id = student_resp.json()["id"]

    get_resp = client.get(f"/students/{student_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == student_id
    assert data["name"] == "Jane"

def test_delete_student():
    school_resp = client.post("/schools/", json={"name": "Test School for Student Deletion"})
    school_id = school_resp.json()["id"]

    student_resp = client.post("/students/", json={"name": "Mark", "school_id": school_id})
    student_id = student_resp.json()["id"]

    del_resp = client.delete(f"/students/{student_id}")
    assert del_resp.status_code == 200
    assert del_resp.json() == {"message": "Estudiante eliminado exitosamente"}

def test_get_student_statement():
    school_resp = client.post("/schools/", json={"name": "Test School for Statement"})
    school_id = school_resp.json()["id"]

    student_resp = client.post("/students/", json={"name": "Lucy", "school_id": school_id})
    student_id = student_resp.json()["id"]

    statement_resp = client.get(f"/students/{student_id}/statement")
    assert statement_resp.status_code == 200
    statements = statement_resp.json()
    assert isinstance(statements, list)
    assert len(statements) == 0  # No invoices yet