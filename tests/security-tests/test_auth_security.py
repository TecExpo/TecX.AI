import requests

BASE_URL = "http://localhost:8000"

def test_brute_force_protection():
    for _ in range(10):  # Simulate 10 failed login attempts
        response = requests.post(f"{BASE_URL}/login", json={"email": "user@example.com", "password": "wrongpassword"})
        assert response.status_code in [401, 429], "Brute force protection failed"

def test_sql_injection():
    payload = "' OR '1'='1' --"
    response = requests.post(f"{BASE_URL}/login", json={"email": payload, "password": "password"})
    assert response.status_code == 401, "SQL Injection vulnerability detected"
