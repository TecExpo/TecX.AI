import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
import torch
from torchvision import transforms

# Define transformation pipeline for images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Function to load and preprocess images
def process_images(image_dir, labels_csv):
    df = pd.read_csv(labels_csv)
    images, labels = [], []

    for _, row in df.iterrows():
        img_path = os.path.join(image_dir, row["filename"])
        if os.path.exists(img_path):
            image = Image.open(img_path).convert("RGB")
            image = transform(image)
            images.append(image)
            labels.append(row["label"])

    return torch.stack(images), torch.tensor(labels)

# Function to split dataset into train, validation, and test sets
def split_dataset(images, labels, test_size=0.2, val_size=0.1):
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=test_size, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, random_state=42)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

# Main execution
if __name__ == "__main__":
    image_dir = "data/images"
    labels_csv = "data/labels.csv"

    images, labels = process_images(image_dir, labels_csv)
    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(images, labels)

    # Save processed datasets
    torch.save((X_train, y_train), "data/train.pt")
    torch.save((X_val, y_val), "data/val.pt")
    torch.save((X_test, y_test), "data/test.pt")

    print("Data preprocessing complete! Train, validation, and test datasets saved.")
