import pytest
from fastapi.testclient import TestClient
from backend.fastapi.main import app
from backend.database.sql.schema import SessionLocal

client = TestClient(app)
db = SessionLocal()

def test_register_and_login():
    register_response = client.post("/register", json={"email": "user@example.com", "password": "password123"})
    assert register_response.status_code == 201

    login_response = client.post("/login", json={"email": "user@example.com", "password": "password123"})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
