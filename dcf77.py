import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs = 200e3
Ts = 1/fs
length_signal = 200e3
bit = 0.2
fill_imp_time_0 = fs * bit
fill_imp_time_1 = fs - fill_imp_time_0
sample_0 = fs * 0.1
sample_1 = fs
minute_sample = fs * 60
fill_imp = 0
signal_length1 = 0
signal_length2 = 0

minute_sample = np.ones(int(minute_sample))

sample_0 = np.zeros(int(sample_0))
sample_1 = np.ones(int(fill_imp_time_1))

impulse = np.hstack((sample_0, sample_1))
while fill_imp < 60:
        signal_length1 = signal_length1 + length_signal
        signal_length2 = signal_length1 + fill_imp_time_0
        minute_sample[int(signal_length1):int(signal_length2)] = 0
        fill_imp += 1

t = np.arange(len(minute_sample)) * Ts
sinus = np.exp(1j * 2 * np.pi * 77500 * t) * 2**15 - 1

out = minute_sample * sinus

out_file = "dcf77_minute.wav"
wavfile.write(out_file, int(fs), out.astype(np.int16))

print(out)
plt.plot(t, out)
plt.grid(True)
plt.show()

