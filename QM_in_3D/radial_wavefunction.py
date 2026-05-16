import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from scipy.special import genlaguerre, factorial

def radial_wavefunction(r, n, l, Z):
    """
    Hydrogen-like radial wave function R_nl(r).
    r in units of a0 (Bohr radius).
    """
    a0 = 1.0  # Bohr radius (atomic units)
    rho = 2 * Z * r / (n * a0)

    norm = np.sqrt(
        (2 * Z / (n * a0))**3
        * factorial(n - l - 1)
        / (2 * n * factorial(n + l)**3)
    )

    L = genlaguerre(n - l - 1, 2 * l + 1)
    return norm * np.exp(-rho / 2) * rho**l * L(rho)


def radial_probability(r, n, l, Z):
    """Radial probability density P(r) = r^2 |R_nl(r)|^2"""
    R = radial_wavefunction(r, n, l, Z)
    return r**2 * R**2


# --- valid (n, l) pairs ---
def valid_l(n):
    return list(range(n))


# --- initial parameters ---
n_init, l_init, Z_init = 2, 1, 1
r_max = 50  # in units of a0

r = np.linspace(0, r_max, 2000)

fig, axes = plt.subplots(2, 1, figsize=(9, 8))
plt.subplots_adjust(left=0.12, right=0.78, hspace=0.4, top=0.93)

ax_R, ax_P = axes

# initial plots
R_line, = ax_R.plot(r, radial_wavefunction(r, n_init, l_init, Z_init), color='steelblue', lw=2)
ax_R.axhline(0, color='k', lw=0.6, ls='--')
ax_R.set_xlabel(r'$r \ (a_0)$')
ax_R.set_ylabel(r'$R_{nl}(r)$')
ax_R.set_title(rf'Radial Wave Function  $R_{{nl}}(r)$  —  n={n_init}, l={l_init}, Z={Z_init}')

P_line, = ax_P.plot(r, radial_probability(r, n_init, l_init, Z_init), color='coral', lw=2)
ax_P.set_xlabel(r'$r \ (a_0)$')
ax_P.set_ylabel(r'$r^2|R_{nl}(r)|^2$')
ax_P.set_title(r'Radial Probability Density  $P(r) = r^2|R_{nl}(r)|^2$')

# ---- widgets ----
ax_Z  = plt.axes([0.82, 0.72, 0.14, 0.18])
ax_n  = plt.axes([0.82, 0.45, 0.14, 0.22])
ax_l  = plt.axes([0.82, 0.20, 0.14, 0.22])

radio_Z = RadioButtons(ax_Z, ['1 (H)', '2 (He⁺)', '3 (Li²⁺)', '4', '5'],
                        active=0, activecolor='steelblue')
radio_n = RadioButtons(ax_n, ['1', '2', '3', '4', '5'],
                        active=1, activecolor='steelblue')
radio_l = RadioButtons(ax_l, ['0', '1', '2', '3', '4'],
                        active=1, activecolor='steelblue')

ax_Z.set_title('Z', fontsize=10, pad=2)
ax_n.set_title('n', fontsize=10, pad=2)
ax_l.set_title('l', fontsize=10, pad=2)

state = {'n': n_init, 'l': l_init, 'Z': Z_init}


def update(_=None):
    n = state['n']
    l = state['l']
    Z = state['Z']

    # clamp l < n
    if l >= n:
        l = n - 1
        state['l'] = l

    r_new = np.linspace(0, 50, 3000)

    R = radial_wavefunction(r_new, n, l, Z)
    P = radial_probability(r_new, n, l, Z)

    R_line.set_data(r_new, R)
    P_line.set_data(r_new, P)

    for ax, data in [(ax_R, R), (ax_P, P)]:
        ax.set_xlim(0, 50)
        margin = 0.1 * (data.max() - data.min()) if data.max() != data.min() else 0.1
        ax.set_ylim(data.min() - margin, data.max() + margin)

    z_labels = {1: '1 (H)', 2: '2 (He⁺)', 3: '3 (Li²⁺)', 4: '4', 5: '5'}
    ax_R.set_title(rf'Radial Wave Function  $R_{{nl}}(r)$  —  n={n}, l={l}, Z={Z}')
    fig.canvas.draw_idle()


def on_Z(label):
    state['Z'] = int(label.split()[0])
    update()

def on_n(label):
    state['n'] = int(label)
    update()

def on_l(label):
    state['l'] = int(label)
    update()

radio_Z.on_clicked(on_Z)
radio_n.on_clicked(on_n)
radio_l.on_clicked(on_l)

plt.suptitle('Hydrogen-like Atom Radial Wave Functions', fontsize=13, fontweight='bold')
plt.show()
