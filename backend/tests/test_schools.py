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

def test_create_school():
    resp = client.post("/schools/", json={"name": "Test School"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Test School"

def test_get_schools():
    resp = client.get("/schools/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_school():
    resp = client.post("/schools/", json={"name": "Another Test School"})
    school_id = resp.json()["id"]

    get_resp = client.get(f"/schools/{school_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == school_id
    assert data["name"] == "Another Test School"

def test_delete_school():
    resp = client.post("/schools/", json={"name": "School to Delete"})
    school_id = resp.json()["id"]

    del_resp = client.delete(f"/schools/{school_id}")
    assert del_resp.status_code == 200
    assert del_resp.json() == {"message": "Escuela eliminada exitosamente"}

def test_get_school_statement():
    resp = client.post("/schools/", json={"name": "Statement Test School"})
    school_id = resp.json()["id"]

    statement_resp = client.get(f"/schools/{school_id}/statement")
    assert statement_resp.status_code == 200
    statements = statement_resp.json()