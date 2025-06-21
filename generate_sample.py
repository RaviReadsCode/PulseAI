import numpy as np

# Generate 360 sample points (1 second of data at 360Hz)
t = np.linspace(0, 1, 360)
# Simulate an ECG-like signal (sinusoidal base + noise)
ecg = 0.6 * np.sin(2 * np.pi * 5 * t) + 0.1 * np.random.randn(360)

# Save to CSV
np.savetxt("sample_ecg.csv", ecg, delimiter="\n")
print("✅ sample_ecg.csv file created with 360 ECG-like values.")
