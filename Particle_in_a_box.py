import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Paramètres initiaux
b0 = 1.0
c1_0 = np.sqrt(5/8)
c2_0 = -np.sqrt(3/8)

def compute(b, c1, c2):
    x = np.linspace(-b, b, 1000)
    psi1 = np.sqrt(1/b) * np.sin(np.pi * (x + b) / (2*b))
    psi2 = np.sqrt(1/b) * np.sin(np.pi * (x + b) / b)
    psi = c1 * psi1 + c2 * psi2
    rho = psi**2
    return x, psi1, psi2, psi, rho

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7))
plt.subplots_adjust(bottom=0.35)

x, psi1, psi2, psi, rho = compute(b0, c1_0, c2_0)

line_psi1, = ax1.plot(x, psi1, label="ψ₁ (fondamental)")
line_psi2, = ax1.plot(x, psi2, label="ψ₂ (excité)")
line_psi,  = ax1.plot(x, psi,  label="ψ superposé")
ax1.axhline(0, color='k', linewidth=0.5)
ax1.set_xlabel("x")
ax1.set_ylabel("ψ(x)")
ax1.set_title("Fonctions d'onde")
ax1.legend()
ax1.grid()

line_rho, = ax2.plot(x, rho, color='tab:orange', label="|ψ(x)|²")
ax2.set_xlabel("x")
ax2.set_ylabel("|ψ|²")
ax2.set_title("Densité de probabilité")
ax2.legend()
ax2.grid()

# Curseurs
ax_b  = plt.axes([0.15, 0.22, 0.70, 0.03])
ax_c1 = plt.axes([0.15, 0.15, 0.70, 0.03])
ax_c2 = plt.axes([0.15, 0.08, 0.70, 0.03])

slider_b  = Slider(ax_b,  'b (demi-largeur)', 0.1, 5.0, valinit=b0)
slider_c1 = Slider(ax_c1, 'c₁', -2.0, 2.0, valinit=c1_0)
slider_c2 = Slider(ax_c2, 'c₂', -2.0, 2.0, valinit=c2_0)

def update(val):
    b  = slider_b.val
    c1 = slider_c1.val
    c2 = slider_c2.val
    x, psi1, psi2, psi, rho = compute(b, c1, c2)

    for line, y in [(line_psi1, psi1), (line_psi2, psi2), (line_psi, psi)]:
        line.set_xdata(x)
        line.set_ydata(y)
    line_rho.set_xdata(x)
    line_rho.set_ydata(rho)

    for ax in (ax1, ax2):
        ax.relim()
        ax.autoscale_view()
    fig.canvas.draw_idle()

slider_b.on_changed(update)
slider_c1.on_changed(update)
slider_c2.on_changed(update)

plt.show()
