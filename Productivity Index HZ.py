# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:03:29 2024

@author: AHernandez
"""

import math

# Function to calculate Productivity Index (PI)
def calculate_productivity_index(kh, mu, B, rw, re, skin):
    """
    Calculate Productivity Index (PI) for a horizontal well in a tight reservoir.

    Parameters:
    - kh: Horizontal permeability (md-ft)
    - mu: Viscosity of fluid (cp)
    - B: Formation volume factor (RB/STB)
    - rw: Wellbore radius (ft)
    - re: Drainage radius (ft)
    - skin: Skin factor

    Returns:
    - PI: Productivity Index (STB/day/psi)
    """
    # Convert permeability from md-ft to darcy-ft
    k = kh * 1.01325
    
    # Calculate PI
    PI = (2.615 * k * B) / (mu * (math.log(re / rw) + skin))
    
    return PI

# Example usage
if __name__ == "__main__":
    # Input parameters (example values)
    kh = 1500  # Horizontal permeability (md-ft)
    mu = 45   # Viscosity of fluid (cp)
    B = 1.045    # Formation volume factor (RB/STB)
    rw = 0.25  # Wellbore radius (ft)
    re = 1000 # Drainage radius (ft)
    skin = 3.0 # Skin factor

    # Calculate PI
    PI = calculate_productivity_index(kh, mu, B, rw, re, skin)

    # Print the calculated PI
    print(f"Productivity Index (PI) = {PI} STB/day/psi")
