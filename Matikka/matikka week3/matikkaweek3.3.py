import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, color="purple", linestyle="--", linewidth=1.5, label="cos(x)")
plt.plot(X, S, color="orange", linestyle=":", linewidth=1.5, label="sin(x)")

plt.xticks(
    [-3 * np.pi, -2 * np.pi, -1.5 * np.pi, -np.pi, -0.5 * np.pi, 0,
     0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi, 3 * np.pi],
    [r'$-3\pi$', r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$',
     r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$3\pi$']
)

plt.yticks(
    [-1, -0.5, 0, 0.5, 1],
    [r'$-1$', r'$-\frac{1}{2}$', r'$0$', r'$\frac{1}{2}$', r'$1$']
)

plt.legend(loc="upper right")

plt.show()
