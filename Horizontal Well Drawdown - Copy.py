# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:05:10 2024

@author: AHernandez
"""

import math

# Function to calculate optimal drawdown to prevent water encroachment
def calculate_optimal_drawdown(kh, mu_oil, mu_water, B_oil, rw, re, h, theta):
    """
    Calculate the optimal drawdown to prevent water encroachment in a horizontal well.

    Parameters:
    - kh: Horizontal permeability (md-ft)
    - mu_oil: Viscosity of oil (cp)
    - mu_water: Viscosity of water (cp)
    - B_oil: Formation volume factor of oil (RB/STB)
    - rw: Wellbore radius (ft)
    - re: Drainage radius (ft)
    - h: Pay zone thickness (ft)
    - theta: Angle of well deviation from horizontal (degrees)

    Returns:
    - optimal_drawdown: Optimal drawdown (psi)
    """
    # Convert permeability from md-ft to darcy-ft
    k = kh * 1.01325
    
    # Calculate critical rate for no water coning
    Q_critical = (2 * math.pi * k * h * B_oil) / (mu_oil * (math.log(re / rw) + theta / (2 * math.tan(math.radians(theta)))))

    # Calculate optimal drawdown
    optimal_drawdown = (mu_water / mu_oil) * (math.log(re / rw) + theta / (2 * math.tan(math.radians(theta)))) / (2 * math.pi * k * h * B_oil)

    return optimal_drawdown

# Example usage
if __name__ == "__main__":
    # Input parameters (example values)
    kh = 1500    # Horizontal permeability (md-ft)
    mu_oil = 45 # Viscosity of oil (cp)
    mu_water = 1.0 # Viscosity of water (cp)
    B_oil = 1.045 # Formation volume factor of oil (RB/STB)
    rw = 0.25    # Wellbore radius (ft)
    re = 1000   # Drainage radius (ft)
    h = 45    # Pay zone thickness (ft)
    theta = 90.0 # Angle of well deviation from horizontal (degrees)

    # Calculate optimal drawdown
    optimal_drawdown = calculate_optimal_drawdown(kh, mu_oil, mu_water, B_oil, rw, re, h, theta)

    # Print the calculated optimal drawdown
    print(f"Optimal Drawdown to prevent water encroachment = {optimal_drawdown} psi")
