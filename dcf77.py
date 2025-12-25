import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import random

freq = 800 #Hz
fs = 200e3
Ts = 1/fs

ft = 645.83 #freq of lfsr
Tt = 1.548338 #duration for 1 chip
N = 512 #length of cycle
Tk = N * Tt #duration of noise cycle

length_signal = 200e3
bit = 0.5
fill_imp_time_0 = fs * bit
fill_imp_time_1 = fs - fill_imp_time_0
sample_0 = fs * 0.1
sample_1 = fs
minute_sample_bits = fs * 60
fill_imp = 0
signal_length1 = 0
signal_length2 = 0

t = np.linspace(0, 60, int(fs * 60), endpoint=False)
minute_sample_bits = np.ones(int(minute_sample_bits))
sample_0 = np.zeros(int(sample_0))
sample_1 = np.ones(int(fill_imp_time_1))
impulse = np.hstack((sample_0, sample_1))

while fill_imp < 60:
        b = random.randint(1, 2)
        if b == 1:
                duty = 0.2
        if b == 2:
                duty = 0.1

        fill_imp_time_0 = fs * duty
        signal_length1 = signal_length1 + length_signal
        signal_length2 = signal_length1 + fill_imp_time_0
        minute_sample_bits[int(signal_length1):int(signal_length2)] = 0.15
        fill_imp += 1

out = minute_sample_bits * np.sin(2 * np.pi * freq * t) * 2 ** 15 - 1
# Save to WAV file
converted_mod_wave = np.int16(out)
wavfile.write("dcf77_minute.wav", fs, converted_mod_wave)

plt.plot(t, out)
plt.grid(True)
plt.show()