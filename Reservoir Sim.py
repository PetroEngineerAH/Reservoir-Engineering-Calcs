# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:22:57 2024

@author: AHernandez
"""

import numpy as np
import matplotlib.pyplot as plt

# Reservoir and simulation parameters
L = 1000.0  # Reservoir length (m)
nx = 100    # Number of grid blocks
dx = L / nx # Grid block size

poro = 0.2        # Porosity
k = 1000.0        # Permeability (mD)
mu = 1.0          # Fluid viscosity (cp)
phi = poro        # Effective porosity
cf = 1e-5         # Fluid compressibility (1/Pa)

# Initial conditions
p_initial = 3000.0  # Initial pressure everywhere (psi)

# Time parameters
dt = 1.0           # Time step (days)
t_final = 500    # Final time (days)
nt = int(t_final / dt)  # Number of time steps

# Create arrays for pressure
p = np.ones(nx) * p_initial

# Main simulation loop
for t in range(nt):
    p_old = np.copy(p)

    # Implicit scheme to solve for new pressures
    for i in range(1, nx-1):
        p[i] = p_old[i] + (dt / (phi * cf)) * (k / mu) * (p_old[i+1] - 2 * p_old[i] + p_old[i-1]) / (dx**2)

    # Boundary conditions (for simplicity, constant pressure at boundaries)
    p[0] = p_initial
    p[-1] = p_initial

# Plotting the pressure profile
x = np.linspace(0, L, nx)
plt.figure(figsize=(10,6))
plt.plot(x, p)
plt.title('1D Reservoir Pressure Profile')
plt.xlabel('Distance (m)')
plt.ylabel('Pressure (psi)')
plt.grid(True)
plt.show()
