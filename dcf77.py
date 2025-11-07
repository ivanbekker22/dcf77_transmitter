import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 12e5, 1)
minute_sample = np.size(n)
imp = np.ones(minute_sample)

rand_bin = np.random.randint(0, 2, size=1)

step = 0
i = 0
fs = 2e5

def null_impulse(bit):
    if bit == 1:
        imp[0:10000] = 0
        imp[200000:220000] = 0
    if bit == 0:
        imp[200000:220000] = 0
        imp[0:10000] = 0
    return imp

null_impulse(bit = rand_bin[0])

plt.plot(n, imp)
plt.grid(True)
plt.show()

