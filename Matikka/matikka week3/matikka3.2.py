import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, color="purple", linestyle="--", linewidth=1.5, label="cos(x)")
plt.plot(X, S, color="orange", linestyle=":", linewidth=1.5, label="sin(x)")

plt.legend(loc="upper right")

plt.show()
