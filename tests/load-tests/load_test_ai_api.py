import requests
import threading

API_URL = "http://localhost:8000/predict"
NUM_REQUESTS = 50  # Simulate 50 AI inference requests

def send_inference_request(request_id):
    sample_input = {"image_url": "https://example.com/sample.jpg"}
    response = requests.post(API_URL, json=sample_input)

    if response.status_code == 200:
        print(f"✅ Request {request_id} completed successfully")
    else:
        print(f"❌ Request {request_id} failed")

threads = []
for i in range(NUM_REQUESTS):
    thread = threading.Thread(target=send_inference_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("✅ Load test for AI API completed.")
