import torch
from ai_models.model import MyAIModel

def test_model_load():
    model = MyAIModel()
    assert model is not None

def test_model_inference():
    model = MyAIModel()
    input_data = torch.randn(1, 3, 224, 224)  # Sample input
    output = model(input_data)
    assert output.shape[0] == 1

if __name__ == "__main__":
    test_model_load()
    test_model_inference()
    print("✅ AI model tests passed.")
