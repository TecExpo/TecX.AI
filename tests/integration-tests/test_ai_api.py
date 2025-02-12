import requests

API_URL = "http://localhost:8000/predict"

def test_ai_model_inference():
    sample_input = {"image_url": "https://example.com/sample.jpg"}
    response = requests.post(API_URL, json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()

if __name__ == "__main__":
    test_ai_model_inference()
    print("✅ AI API integration test passed.")
