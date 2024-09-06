# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:48:19 2024

@author: ahernandez
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants and reservoir properties
k = 210.0           # md (as float)
mu = 1.5            # cp (as float)
B = 1.0             # RB/STB (as float)
phi = 0.21
delta_x = 375.0     # ft (as float)
delta_y = 450.0     # ft (as float)
h = 55.0            # ft (as float)
q4 = 600.0          # STB/D (production rate in block 4) as float
P1 = 3725.0         # psia (pressure in block 1) as float
P5 = 1200.0         # psia (pressure in block 5) as float

# Flow area (A)
A = h * delta_y  # ft² (as float)

# Corrected transmissibility calculation
# Convert permeability to consistent units (md to ft^2)
k_ft2 = k * 9.869233e-16  # md to ft² (as float)

# Transmissibility formula in consistent units (STB/D/psi)
T = (k_ft2 * A) / (mu * B * delta_x) * 5.615  # Multiplied by 5.615 to convert to STB/D/psi (as float)

# Initial pressures in each block
P = np.array([P1, 3500.0, 3300.0, 3100.0, P5])  # Estimate initial pressures (as float)

# Simulation parameters
max_iter = 1000
tolerance = 1e-5
n_time_steps = 50  # Number of time steps

# Lists to store results for plotting
pressure_evolution = []
flow_left_block_1_evolution = []
flow_right_block_5_evolution = []

# Iterative solution (Gauss-Seidel-like) over multiple time steps
def solve_pressure(P, q4, T, P1, P5):
    for _ in range(max_iter):
        P_new = np.copy(P)
        
        # Update pressures for interior blocks (2, 3, 4)
        P_new[1] = 0.5 * (P[0] + P[2])  # Block 2
        P_new[2] = 0.5 * (P[1] + P[3])  # Block 3
        P_new[3] = (0.5 * (P[2] + P[4]) + q4 / T)  # Block 4 with well production
        
        # Boundary conditions (blocks 1 and 5 pressures fixed)
        P_new[0] = P1  # Block 1
        P_new[4] = P5  # Block 5

        # Check for convergence
        if np.max(np.abs(P_new - P)) < tolerance:
            break
        
        P = P_new
    
    return P

# Simulate over time steps
for t in range(n_time_steps):
    P = solve_pressure(P, q4, T, P1, P5)
    
    # Store pressure and flow rate results at each time step
    pressure_evolution.append(P.copy())
    
    # Calculate flow rates across boundaries of blocks 1 and 5
    flow_left_block_1 = T * (P[0] - P[1])  # Flow at left boundary of Block 1
    flow_right_block_5 = T * (P[3] - P[4])  # Flow at right boundary of Block 5
    
    flow_left_block_1_evolution.append(flow_left_block_1)
    flow_right_block_5_evolution.append(flow_right_block_5)
    
    print(flow_left_block_1)
    print(flow_right_block_5)

# Convert to arrays for easy plotting
pressure_evolution = np.array(pressure_evolution)
flow_left_block_1_evolution = np.array(flow_left_block_1_evolution)
flow_right_block_5_evolution = np.array(flow_right_block_5_evolution)

# Plot the pressure distribution across the blocks over time
plt.figure(figsize=(10, 6))

for i in range(5):  # 5 blocks
    plt.plot(range(n_time_steps), pressure_evolution[:, i], label=f'Block {i+1}')

plt.title("Pressure Distribution Across Blocks Over Time")
plt.xlabel("Time Step")
plt.ylabel("Pressure (psia)")
plt.legend()
plt.grid(True)
plt.show()

# Plot the flow rates across block boundaries over time
plt.figure(figsize=(10, 6))

plt.plot(range(n_time_steps), flow_left_block_1_evolution, label='Flow at Left Boundary of Block 1')
plt.plot(range(n_time_steps), flow_right_block_5_evolution, label='Flow at Right Boundary of Block 5')

plt.title("Flow Rates Across Block Boundaries Over Time")
plt.xlabel("Time Step")
plt.ylabel("Flow Rate (STB/D)")
plt.legend()
plt.grid(True)
plt.show()
