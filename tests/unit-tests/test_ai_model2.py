import pytest
from backend.ai_models.inference import predict

def test_ai_model_prediction():
    sample_input = {"text": "Hello, world!"}
    output = predict(sample_input)
    
    assert output is not None
    assert isinstance(output, dict)
    assert "prediction" in output
