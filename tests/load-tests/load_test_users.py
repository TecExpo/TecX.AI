import requests
import threading

BASE_URL = "http://localhost:8000"  # Adjust for FastAPI backend
NUM_USERS = 100  # Simulate 100 concurrent users

def register_and_login(user_id):
    user_data = {
        "username": f"user{user_id}",
        "email": f"user{user_id}@example.com",
        "password": "securepassword"
    }
    
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    if response.status_code != 201:
        print(f"❌ Registration failed for user{user_id}")
        return

    login_data = {"email": user_data["email"], "password": user_data["password"]}
    login_response = requests.post(f"{BASE_URL}/login", json=login_data)
    
    if login_response.status_code == 200:
        print(f"✅ User{user_id} logged in successfully")
    else:
        print(f"❌ Login failed for user{user_id}")

threads = []
for i in range(NUM_USERS):
    thread = threading.Thread(target=register_and_login, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("✅ Load test for user authentication completed.")
