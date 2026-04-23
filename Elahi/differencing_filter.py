import numpy as np
import matplotlib.pyplot as plt

# =========================
# Given parameters
# =========================
fs = 100
f  = 10
T  = 1
t  = np.arange(0, T, 1/fs)

# =========================
# Generate noisy signal
# =========================
np.random.seed(0)
signal = np.sin(2 * np.pi * f * t)
noise  = 0.5 * np.random.randn(len(t))
noisy  = signal + noise

# =========================
# 6-point differencing filter
# y[n] = (1/6) * (x[n] + x[n-1] + x[n-2] + x[n-3] + x[n-4] + x[n-5])
# =========================
h = np.ones(6) / 6
filtered = np.convolve(noisy, h, mode='same')

# =========================
# Plotting
# =========================
plt.figure(figsize=(12, 8))

# Original clean signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, color='green')
plt.title("Original Signal (10 Hz Sine Wave)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Noisy signal
plt.subplot(3, 1, 2)
plt.plot(t, noisy, color='red', alpha=0.8)
plt.title("Noisy Signal (Sine + White Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Filtered signal
plt.subplot(3, 1, 3)
plt.plot(t, noisy,    color='red',   alpha=0.4, label='Noisy')
plt.plot(t, filtered, color='blue',  linewidth=2, label='Filtered')
plt.title("Filtered Signal (6-Point Differencing Filter)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
