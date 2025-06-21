import wfdb
import numpy as np

def extract_heartbeats(record_name='100', window_size=360):
    record = wfdb.rdrecord(record_name, pn_dir='mitdb')
    annotation = wfdb.rdann(record_name, 'atr', pn_dir='mitdb')

    signal = record.p_signal[:, 0]  # Use MLII
    r_peaks = annotation.sample

    beats = []
    for r in r_peaks:
        start = r - window_size // 2
        end = r + window_size // 2
        if start >= 0 and end <= len(signal):
            beat = signal[start:end]
            beats.append(beat)

    return np.array(beats)  # Shape: (num_beats, window_size)
