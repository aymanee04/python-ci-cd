import requests


BASE_URL = "http://localhost:5000"


def test_health():
    response = requests.get(f"{BASE_URL}/api/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"


def test_users():
    response = requests.get(f"{BASE_URL}/api/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["id"] == 1