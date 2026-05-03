import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(0, 4 * np.pi, 10000)

# |cos(alpha)| quand tan(alpha) > 0, |sin(alpha)| sinon
tan_positive = np.tan(alpha) > 0
f = np.where(tan_positive, np.abs(np.cos(alpha)), np.abs(np.sin(alpha)))

plt.figure(figsize=(10, 4))
plt.plot(alpha, f, color='tab:blue')
plt.xlabel("α")
plt.ylabel("f(α)")
plt.title("|cos α| si tan α > 0,   |sin α| sinon")
plt.xticks(
    [k * np.pi / 2 for k in range(9)],
    [r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$",
     r"$5\pi/2$", r"$3\pi$", r"$7\pi/2$", r"$4\pi$"]
)
plt.ylim(0, 1.1)
plt.grid()
plt.tight_layout()
plt.show()
