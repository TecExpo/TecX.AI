import requests

BASE_URL = "http://localhost:8000"

def test_xss_in_user_profile():
    xss_payload = "<script>alert('XSS')</script>"
    user_data = {"username": xss_payload, "email": "test@example.com", "password": "securepassword"}

    response = requests.post(f"{BASE_URL}/register", json=user_data)

    if xss_payload in response.text:
        print("❌ XSS vulnerability detected in user profile!")
    else:
        print("✅ XSS test passed for user profile.")

test_xss_in_user_profile()
