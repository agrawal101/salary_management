import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_employee():
    payload = {
        "full_name": "Gaurav Agrawal",
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
        "full_name": "Gaurav Agrawal",
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
    assert data["full_name"] == "Gaurav Agrawal"

# def test_get_employee_by_invalid_id():
#     response = client.get("/employees/999999")

#     assert response.status_code == 404

def test_get_all_employees():
    employees = [
        {
            "full_name": "Gaurav Agrawal",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000
        },
        {
            "full_name": "Jane Smith",
            "job_title": "QA Engineer",
            "country": "India",
            "salary": 80000
        }
    ]

    for employee in employees:
        client.post("/employees", json=employee)

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 2

    

def test_get_all_employees_with_pagination():
    employees = [
        {
            "full_name": "Gaurav Agrawal",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000
        },
        {
            "full_name": "Jane Smith",
            "job_title": "QA Engineer",
            "country": "India",
            "salary": 80000
        }
    ]

    for employee in employees:
        client.post("/employees", json=employee)

    response = client.get("/employees?page=1&size=10")

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 2

def test_get_employees_invalid_page():
    response = client.get("/employees?page=0&size=10")

    assert response.status_code == 422

def test_get_employees_invalid_size():
    response = client.get("/employees?page=1&size=0")

    assert response.status_code == 422

def test_update_employee():
    payload = {
        "full_name": "Gaurav Agrawal",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000
    }

    create_response = client.post(
        "/employees",
        json=payload
    )

    employee_id = create_response.json()["id"]

    update_payload = {
        "full_name": "Gaurav Updated",
        "job_title": "Senior Engineer",
        "country": "India",
        "salary": 150000
    }

    response = client.put(
        f"/employees/{employee_id}",
        json=update_payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["full_name"] == "Gaurav Updated"
    assert data["job_title"] == "Senior Engineer"
    assert data["salary"] == 150000