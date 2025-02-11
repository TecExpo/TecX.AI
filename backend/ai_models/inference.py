import tensorflow as tf
import numpy as np
from model import create_model

# Load or create the model
model = create_model()
model.load_weights("model_weights.h5")  # Load pre-trained weights if available

# Sample input for inference
def predict(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return float(prediction[0][0])

if __name__ == "__main__":
    sample_input = [0.5] * 10  # Example input
    print("Prediction:", predict(sample_input))
