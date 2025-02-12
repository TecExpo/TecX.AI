import pytest
from backend.fastapi.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"email": "test@example.com", "password": "secure123"})
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"

def test_login_user():
    response = client.post("/login", json={"email": "test@example.com", "password": "secure123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route_without_auth():
    response = client.get("/protected-route")
    assert response.status_code == 401  # Unauthorized access should be blocked
