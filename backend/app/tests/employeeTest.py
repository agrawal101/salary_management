def test_create_employee():
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 100000
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 201