import tensorflow as tf
from tensorflow import keras

# Define a simple AI model
def create_model():
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(10,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

if __name__ == "__main__":
    model = create_model()
    model.summary()
