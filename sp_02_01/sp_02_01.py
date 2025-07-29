# Supplemental Program 2.1 (Python Version)
# -----------------------------------------
# Calculate and graph leaf area density profiles
# -----------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta as beta_function

# --- Parameters for beta distribution
p_values = [2.5, 3.5, 11.5]
q_values = [2.5, 2.0, 3.5]

# --- Canopy parameters
LAI = 5.0   # Leaf area index (m²/m²)
hc = 10.0   # Canopy height (m)

print(f"Leaf area index = {LAI:.2f}")

# --- Create height vector z
z_min = 0.0
z_max = hc
dz = 0.1
z = np.arange(z_min, z_max + dz, dz)

# --- Initialize storage for LAD profiles
lad_profiles = []

# Loop over each (p, q) parameter pair
for p, q in zip(p_values, q_values):
    lad = np.zeros_like(z)
    total_lai = 0.0

    for i, height in enumerate(z):
        x = height / hc
        lad[i] = (LAI / hc) * (x ** (p - 1) * (1 - x) ** (q - 1)) / beta_function(p, q)
        total_lai += lad[i] * dz

    lad_profiles.append(lad)

    print(f"p, q = {p:6.2f}, {q:6.2f}")
    print(f"Leaf area index (numerical) = {total_lai:8.4f}")

# --- Plotting
z_rel = z / hc

plt.plot(lad_profiles[0], z_rel, 'b-', label='p,q = 2.5,2.5')
plt.plot(lad_profiles[1], z_rel, 'r-', label='p,q = 3.5,2.0')
plt.plot(lad_profiles[2], z_rel, 'g-', label='p,q = 11.5,3.5')

plt.title("Leaf Area Density Profiles")
plt.xlabel("Leaf area density (m² m⁻³)")
plt.ylabel("Relative height (z/hₐ)")
plt.legend(loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.show()
