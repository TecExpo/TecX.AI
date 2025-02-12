import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

# Define model architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.model = models.resnet18(pretrained=False)
        self.model.fc = nn.Linear(512, 10)  # Same as training model

    def forward(self, x):
        return self.model(x)

# Load trained model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleCNN().to(device)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Function for inference
def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)  # Add batch dimension

    with torch.no_grad():
        output = model(image)
        _, predicted_class = torch.max(output, 1)

    return f"Predicted Class: {predicted_class.item()}"

# Example Usage
if __name__ == "__main__":
    image_path = "test_image.jpg"  # Replace with actual image path
    prediction = predict(image_path)
    print(prediction)
