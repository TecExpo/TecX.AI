import requests

BASE_URL = "http://localhost:8000"  # Adjust for FastAPI backend

def test_user_registration_and_login():
    user_data = {"username": "testuser", "email": "test@example.com", "password": "securepassword"}
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    assert response.status_code == 201
    user_id = response.json().get("user_id")

    login_data = {"email": "test@example.com", "password": "securepassword"}
    login_response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")

    headers = {"Authorization": f"Bearer {token}"}
    profile_response = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert profile_response.status_code == 200
    assert profile_response.json()["email"] == "test@example.com"

if __name__ == "__main__":
    test_user_registration_and_login()
    print("✅ User flow test passed.")
├── integration-tests/ # API and full-system tests
