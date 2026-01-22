import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import random

state = 0b100000000

freq = 77500  # Hz
fs = 200e3
Ts = 1 / fs

ft = 645.83  # freq of lfsr
Tt = 0.001548338  # duration for 1 chip
N = 512  # length of cycle
Tk = N * Tt  # duration of noise cycle

length_signal = 200e3
fill_imp = 0
s1 = 0
s2 = 0
s1_1 = 0
s2_1 = 0
len_s = 0.001548338
lfsr_cnt = 0

minute_sample_bits = fs * 60
t = np.linspace(0, 60, int(fs * 60), endpoint=False)
minute_sample_bits = np.ones(int(minute_sample_bits))


def linfsr(state, b):
    global databit
    global s1
    global lfsr_cnt
    global phase
    for i in range(512):
        lfsr_bit = np.array(state & 1)
        # print(lfsr_bit, end='')
        newbit = (state ^ (state >> 4) ^ (state >> 9)) & 1
        state = (state >> 1) | (newbit << 8)
        databit = b ^ lfsr_bit
        if databit == 0:
            phase = 15.6
            s1 = s1 + 390.625
            s2 = s1 + 390.625 * 1
            minute_sample_bits[int(s1):int(s2)] = 0.15
        if databit == 1:
            phase = -15.6
            s1 = s1 + 390.625
            s2 = s1 + 390.625 * 0.5
            minute_sample_bits[int(s1):int(s2)] = 0.15
        print(databit, end='')
        lfsr_cnt += 1
    lfsr_cnt = 0
    return databit


while fill_imp < 60:
    global duty
    b = random.randint(0, 1)
    if b == 0:
        duty = 0.2
    if b == 1:
        duty = 0.1

    fill_imp_time_0 = fs * duty
    s1_1 = s1_1 + length_signal
    s2_1 = s1_1 + fill_imp_time_0
    minute_sample_bits[int(s1_1):int(s2_1)] = 0.15
    fill_imp += 1
fill_imp = 0

for i in range(60):
    linfsr(state, b)

out = minute_sample_bits * np.sin((2 * np.pi / phase) * freq * t) * 2 ** 15 - 1
# Save to WAV file
wavfile.write("dcf77_minute.wav", 200000, out.astype(np.int16))

plt.plot(t, out)
plt.grid(True)
plt.show()
