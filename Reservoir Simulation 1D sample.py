# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:42:31 2024

@author: ahernandez
"""

import numpy as np
#Sample includes 1D reservoir with five blocks, each having a well producing 600STB/d. 
#Continuation: the boundary pressure are given for blocks 1 and 5. 
#Continuation: the goal of this excercise is to find the pressure distribution across the reservoir and estimate the rates of oil loss or gain across the boundaries of block 5 and 1. 
# Constants and reservoir properties
k = 210           # md
mu = 1.5          # cp
B = 1.0           # RB/STB
phi = 0.21
delta_x = 375     # ft
delta_y = 450     # ft
h = 55            # ft
q4 = 600          # STB/D (production rate in block 4)
P1 = 3725         # psia (pressure in block 1)
P5 = 1200         # psia (pressure in block 5)

# Calculate transmissibility (psi/STB/day)
T = (k * h * delta_y) / (mu * B * delta_x) * 6.33e-3  # Convert to consistent units

# Initialize pressure in each block (initial guess)
P = np.array([P1, (P1 + P5) / 2, (P1 + P5) / 2, (P1 + P5) / 2, P5])

# Maximum iterations and tolerance
max_iter = 1000
tolerance = 1e-5

# Iterative solution (Jacobi or Gauss-Seidel Method)
def solve_pressure(P, q4, T, P1, P5):
    for _ in range(max_iter):
        P_new = np.copy(P)
        
        # Update pressures for interior blocks (2, 3, 4)
        P_new[1] = 0.5 * (P[0] + P[2])  # Block 2
        P_new[2] = 0.5 * (P[1] + P[3])  # Block 3
        P_new[3] = 0.5 * (P[2] + P[4] + q4 / T)  # Block 4 with well production
        
        # Boundary conditions (blocks 1 and 5 pressures fixed)
        P_new[0] = P1  # Block 1
        P_new[4] = P5  # Block 5

        # Check for convergence
        if np.max(np.abs(P_new - P)) < tolerance:
            break
        
        P = P_new
    
    return P

# Solve for pressures in all blocks
P_solution = solve_pressure(P, q4, T, P1, P5)

# Output the pressure distribution
print("Pressure distribution in the blocks:", P_solution)

# Calculate flow rates across block boundaries
# Flow from left of block 1 (Block 1 -> Block 2)
flow_left_block_1 = T * (P_solution[0] - P_solution[1])

# Flow from right of block 5 (Block 4 -> Block 5)
flow_right_block_5 = T * (P_solution[3] - P_solution[4])

# Output flow rates
print(f"Flow rate across the left boundary of block 1: {flow_left_block_1:.2f} STB/D")
print(f"Flow rate across the right boundary of block 5: {flow_right_block_5:.2f} STB/D")
