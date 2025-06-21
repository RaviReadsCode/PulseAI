import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential  # ✅ fixed import
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import joblib
import os

# Import your data loader
from app.data_preparation import get_data

# Step 1: Load and preprocess data
(X_train, X_test, y_train, y_test), encoder = get_data()

# Step 2: Define the model
model = Sequential([
    Conv1D(32, 3, activation='relu', input_shape=(X_train.shape[1], 1)),
    MaxPooling1D(2),
    Conv1D(64, 3, activation='relu'),
    MaxPooling1D(2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(y_train.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 3: Train the model
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Step 4: Save the model and encoder
os.makedirs("models", exist_ok=True)
model.save("models/pulseai_cnn.h5")
joblib.dump(encoder, "models/label_encoder.pkl")

print("✅ Model and encoder saved successfully.")
