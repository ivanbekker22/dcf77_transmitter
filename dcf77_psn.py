import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import random

state = 0b100000000
freq = 77500  # Hz
fs = 200e3
length_signal = 200e3
s1 = 0
s2 = 0
s1_1 = 0
s2_1 = 0

minute_sample_bits = fs * 60
t = np.linspace(0, 60, int(fs * 60), endpoint=False)
minute_sample_bits = np.ones(int(minute_sample_bits))


def lin_fsr(state, b, s1):
    for i in range(512):
        lfsr_bit = state & 1
        databit = b ^ lfsr_bit
        newbit = (state ^ (state >> 4) ^ (state >> 9)) & 1
        state = (state >> 1) | (newbit << 8)
        print(databit, end='')
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
    return databit, phase, s1


def minute_fill(s1_1):
    b = random.randint(0, 1)
    if b == 0:
        duty = 0.2
    if b == 1:
        duty = 0.1
    fill_imp_time_0 = fs * duty
    s1_1 = s1_1 + length_signal
    s2_1 = s1_1 + fill_imp_time_0
    minute_sample_bits[int(s1_1):int(s2_1)] = 0.15
    return s1_1, duty, b


if __name__ == "__main__":
    for i in range(60):
        s1_1, duty, b = minute_fill(s1_1)
        databit, phase, s1 = lin_fsr(state, b, s1)

    out = minute_sample_bits * np.sin((phase * np.pi / 180) * freq * t) * 2 ** 15 - 1
    wavfile.write("dcf77_minute.wav", 200000, out.astype(np.int16))

    plt.plot(t, out)
    plt.grid(True)
    plt.show()
