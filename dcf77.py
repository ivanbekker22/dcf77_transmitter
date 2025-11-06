import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 12000000, 1)
length = np.size(n)
imp0 = np.zeros(length)
def impl0():
    val = np.where((n >= 20000) & (n <= 200000))
    imp0[val] = 1
    return imp0



plt.plot(n, imp0)
plt.grid(True)
plt.show()

