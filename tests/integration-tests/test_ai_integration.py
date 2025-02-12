import pytest
from backend.ai_models.inference import predict

def test_ai_pipeline():
    input_data = {"text": "How is the weather today?"}
    response = predict(input_data)

    assert response is not None
    assert "prediction" in response
