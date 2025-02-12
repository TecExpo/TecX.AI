import requests

BASE_URL = "http://localhost:8000"

def test_access_protected_resource_without_auth():
    response = requests.get(f"{BASE_URL}/protected-resource")

    if response.status_code == 200:
        print("❌ Authentication bypass detected! Unauthenticated access to protected resource.")
    else:
        print("✅ Authentication test passed. Unauthorized access blocked.")

test_access_protected_resource_without_auth()
