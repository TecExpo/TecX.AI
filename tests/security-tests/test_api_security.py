import requests

BASE_URL = "http://localhost:8000"

def test_unauthorized_access():
    response = requests.get(f"{BASE_URL}/dashboard")
    assert response.status_code == 401, "Unauthorized access should be blocked"

def test_token_expiry():
    token = "expired_or_fake_token"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/dashboard", headers=headers)
    assert response.status_code == 401, "Expired tokens should be rejected"
