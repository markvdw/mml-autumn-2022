import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

mpl.rcParams["figure.dpi"] = 200

noise_mean = 0.1
noise_std = 0.1
amplitude_func = lambda f: 5.0 * np.exp(-((f - 2.8)/0.8)**2) + np.random.randn(len(f) if type(f) is np.ndarray else 1) * noise_std + noise_mean
# Idea: have something looking more like a 2nd order resonant system. This way you have more control over the width of the peak. Fundamentally not symmetric though.

# freq = np.exp(np.random.randn(1000) * 0.1 + 1.0)
# plt.hist(freq, bins=50, density=True)
# X = np.linspace(0.01, 5, 1000)
# plt.plot(X, amplitude_func(X))
# plt.hist(amplitude_func(freq), bins=50, density=True)

# Data generating process
data = []
latent = []
freqs = []
for _ in range(1000):
    if np.random.rand() < 0.3:
        latent.append(0)
        data.append(np.random.randn() * noise_std + noise_mean + 0.3)
        freqs.append(np.nan)
    else:
        latent.append(1)
        freq = np.exp(np.random.randn() * 0.15 + 1.0)
        data.append(
            amplitude_func(freq)
        )
        freqs.append(freq)
data = np.vstack((np.hstack(latent), np.hstack(data), np.hstack(freqs))).T

plt.figure(figsize=(8, 3))
_, bins, _ = plt.hist(data[:, 1], bins=50, density=True, label="Empirical data", alpha=0.2)
kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(data[:, 1, None])
kde_plot_X = np.linspace(0, 5.5, 500)[:, None]
density = kde.score_samples(kde_plot_X)
plt.plot(kde_plot_X, np.exp(density), 'C0', label="KDE estimate $p(y)$")
plt.xlabel("Amplitude $y$ (mm)")
plt.ylabel("Prob density $p(y)$ ($\mathrm{mm}^{-1}$)")
plt.legend()
plt.tight_layout()
xlim = plt.xlim()
plt.savefig("resonance-marginal-histogram.png")

plt.figure(figsize=(8, 3))
# Argh, not sure how to plot two different colours of histograms that are normalised to a single density.
# https://stackoverflow.com/questions/47999159/normalizing-two-histograms-in-the-same-plot
plt.hist(data[data[:, 0] == 1, 1], bins=bins, label="Empirical data, C=1")
plt.hist(data[data[:, 0] == 0, 1], bins=bins, label="Empirical data, C=0")
plt.xlabel("Amplitude $y$ (mm)")
plt.ylabel("Occurrences")
plt.xlim(*xlim)
plt.legend()
plt.tight_layout()
plt.savefig("resonance-cond-histogram.png")

plt.figure(figsize=(8, 3))
# Argh, not sure how to plot two different colours of histograms that are normalised to a single density.
# https://stackoverflow.com/questions/47999159/normalizing-two-histograms-in-the-same-plot
plt.hist(data[data[:, 0] == 1, 1], bins=bins, density=True, label="Empirical data, C=1", alpha=0.2)
plt.hist(data[data[:, 0] == 0, 1], bins=bins, density=True, label="Empirical data, C=0", alpha=0.2)
kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(data[data[:, 0] == 1, 1, None])
kde_plot_X = np.linspace(0, 5.5, 500)[:, None]
density = kde.score_samples(kde_plot_X)
plt.plot(kde_plot_X, np.exp(density), 'C0', label="KDE estimate $p(y|C=1)$")
kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(data[data[:, 0] == 0, 1, None])
kde_plot_X = np.linspace(0, 5.5, 500)[:, None]
density = kde.score_samples(kde_plot_X)
plt.plot(kde_plot_X, np.exp(density), 'C1', label="KDE estimate $p(y|C=0)$")
plt.xlabel("Amplitude $y$ (mm)")
plt.ylabel("Prob density $p(y|C)$ ($\mathrm{mm}^{-1}$)")
plt.legend()
plt.tight_layout()
plt.savefig("resonance-cond-probs.png")

fig, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 3]}, figsize=(8, 3), sharey=True)
ax2.plot(data[data[:, 0] == 1, 2], data[data[:, 0] == 1, 1], 'x')
ax2.set_xlim(0, 5)
ax2.set_xlabel("Frequency $x$ (Hz)")
# plt.legend()
ax1.hist(data[data[:, 0] == 1, 1], bins=bins, density=True, label="Empirical data, C=1", orientation="horizontal")
ax1.set_ylabel("Amplitude $y$ (mm)")
ax1.set_xlabel("Prob density $p(y)$ ($\mathrm{mm}^{-1}$)")
plt.tight_layout()
plt.savefig("resonance-regression.png")



# density = lambda x: (2*np.pi*std1**2.0)**-0.5 * np.exp(-((x-0.1)/std1)**2.0) + (2*np.pi*std2**2.0)**-0.5 * np.exp(-((x-1.0)/std2)**2.0)

# X = np.linspace(0.01, 5, 1000)

# plt.plot(X, density(X))


