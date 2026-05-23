import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_employee():
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000
    }
    response = client.post("/employees", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == payload["full_name"]
    assert data["job_title"] == payload["job_title"]
    assert data["country"] == payload["country"]
    assert data["salary"] == payload["salary"]
    assert "id" in data

def test_get_employee_by_id():
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000
    }
    create_response = client.post("/employees", json=payload)
    assert create_response.status_code == 201
    employee_id = create_response.json()["id"]
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["full_name"] == "John Doe"