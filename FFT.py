import numpy as np
import matplotlib.pyplot as plt
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)
S = np.fft.fft(s)
plt.plot(s)