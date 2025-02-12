import requests

BASE_URL = "http://localhost:8000"

def test_sql_injection_login():
    payload = {"email": "' OR '1'='1", "password": "anything"}
    response = requests.post(f"{BASE_URL}/login", json=payload)

    if response.status_code == 200:
        print("❌ Potential SQL Injection vulnerability detected in login endpoint!")
    else:
        print("✅ SQL Injection test passed for login endpoint.")

def test_sql_injection_user_fetch():
    injection_payload = "' OR 1=1 --"
    response = requests.get(f"{BASE_URL}/users/{injection_payload}")

    if response.status_code == 200:
        print("❌ Potential SQL Injection vulnerability detected in user fetch!")
    else:
        print("✅ SQL Injection test passed for user fetch.")

test_sql_injection_login()
test_sql_injection_user_fetch()
