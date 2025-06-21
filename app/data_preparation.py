import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

def get_data():
    # Simulate 1000 ECG signals, each 360 samples long (1-second window)
    num_samples = 1000
    signal_length = 360

    # Create random ECG-like data
    X = np.random.randn(num_samples, signal_length).astype(np.float32)

    # Simulate labels (3 classes: Normal, Arrhythmia, PVC)
    labels = np.random.choice(['Normal', 'Arrhythmia', 'PVC'], size=num_samples)

    # Reshape for Conv1D input: (samples, timesteps, features)
    X = X[..., np.newaxis]

    # Encode labels
    encoder = LabelEncoder()
    y = encoder.fit_transform(labels)
    y = to_categorical(y)  # convert to one-hot vectors

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return (X_train, X_test, y_train, y_test), encoder
