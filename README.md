# Quantum Mechanics 1

Interactive Python models illustrating basic quantum mechanics principles: infinite square wells, hydrogen-like atomic orbitals, and finite potential well quantization.

## Contents

| Script | Description |
|---|---|
| [`Particle_in_a_box.py`](Particle_in_a_box.py) | Infinite square well ("particle in a box"). Plots the ground and first excited stationary states and their superposition, with the resulting probability density. Sliders control the well half-width `b` and the superposition coefficients `c1`, `c2`. |
| [`QM_in_3D/radial_wavefunction.py`](QM_in_3D/radial_wavefunction.py) | Hydrogen-like atom radial wave functions `R_nl(r)` and radial probability density `P(r) = r²\|R_nl(r)\|²`, computed from the generalized Laguerre polynomials. Radio buttons select the quantum numbers `n`, `l` and nuclear charge `Z`. |
| [`finite_potential_well/quantification_condition_for_even_functions.py`](finite_potential_well/quantification_condition_for_even_functions.py) | Plots the transcendental quantization condition for the even bound states of a finite square well, used to graphically locate allowed energy levels. |

## Requirements

- Python 3
- `numpy`
- `scipy`
- `matplotlib`

Install with:

```bash
pip install numpy scipy matplotlib
```

## Usage

Each script is standalone and opens an interactive `matplotlib` window:

```bash
python Particle_in_a_box.py
python QM_in_3D/radial_wavefunction.py
python finite_potential_well/quantification_condition_for_even_functions.py
```
