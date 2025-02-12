import requests
import threading

BASE_URL = "http://localhost:8000"

def send_request():
    response = requests.post(f"{BASE_URL}/login", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200

def test_api_load():
    threads = []
    for _ in range(100):  # Simulate 100 concurrent users
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
