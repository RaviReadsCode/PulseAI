import numpy as np
from tensorflow.keras.models import load_model
import joblib

model = load_model("models/pulseai_cnn.h5")
encoder = joblib.load("models/label_encoder.pkl")

def predict(signal: np.ndarray) -> str:
    signal = signal.reshape(1, -1, 1)
    pred = model.predict(signal)
    label = encoder.inverse_transform([np.argmax(pred)])
    return label[0]
