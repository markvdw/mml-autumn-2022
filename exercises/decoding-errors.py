import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

pi = 0.6
p = np.linspace(0, 1, 100)
s = 1
t = s**2 * np.log((1-p)/p) + 0.5

P = pi * (1 - norm.cdf((t - 1) / s)) + (1-pi)*norm.cdf(t/s)
plt.plot(p, P)
plt.grid()
plt.xlabel("$P(S=1) = p$")
plt.ylabel("$P(\hat S = S)$")
plt.savefig("elec-decoding-errors.png")
