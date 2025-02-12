import requests

BASE_URL = "http://localhost:8000"  # Change this based on your backend

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_user_registration():
    user_data = {"username": "testuser", "email": "test@example.com", "password": "securepassword"}
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    assert response.status_code == 201
    assert "user_id" in response.json()

def test_user_login():
    login_data = {"email": "test@example.com", "password": "securepassword"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

if __name__ == "__main__":
    test_health_check()
    test_user_registration()
    test_user_login()
    print("✅ All API tests passed.")
