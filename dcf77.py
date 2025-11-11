import numpy as np
import matplotlib.pyplot as plt

fs = 200e3
length_signal = 200e3
bit = 0.1
fill_imp_time_0 = fs * bit
fill_imp_time_1 = fs - fill_imp_time_0
sample_0 = fs * 0.1
sample_1 = fs
minute_sample = fs * 60
Ts = 1/fs
fill_imp = 0
signal_length1 = 0
signal_length2 = 0

minute_sample = np.ones(int(minute_sample))

sample_0 = np.zeros(int(sample_0))
sample_1 = np.ones(int(fs))

impulse = np.hstack((sample_0, sample_1))

while fill_imp < 60:
    if fill_imp == 0:
        length_signal = 0
        signal_length1 = signal_length1 + length_signal
        signal_length2 = signal_length1 + fill_imp_time_0
        minute_sample[int(signal_length1):int(signal_length2)] = 0
        fill_imp += 1
    else:
        length_signal = 200e3
        signal_length1 = signal_length1 + length_signal
        signal_length2 = signal_length1 + fill_imp_time_0
        minute_sample[int(signal_length1):int(signal_length2)] = 0
        fill_imp += 1

print(minute_sample)
plt.plot(minute_sample)
plt.grid(True)
plt.show()

