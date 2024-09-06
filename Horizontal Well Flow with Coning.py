# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 08:05:03 2024

@author: AHernandez
"""

import math 

# Input parameters for production rate calculation using Joshi's method
permeability = 100  # Permeability in millidarcies (mD)
NetPay = 50  # Reservoir thickness in feet
BHP = 2100  # Pressure drawdown in psi
viscosity = 35  # Oil viscosity in centipoise (cp)
well_length = 2000  # Horizontal well length in feet
well_radius = 0.25  # Wellbore radius in feet
drainage_radius = 1000  # Drainage radius in feet

# Input parameters for water coning prevention calculation
oil_column_height = 50  # Height of oil column in feet
water_column_height = 200  # Height of water column in feet
oil_density = 62  # Density of oil in lb/ft³
water_density = 62.4  # Density of water in lb/ft³
oil_permeability = 100  # Permeability in the oil zone in millidarcies (mD)
water_permeability = 100  # Permeability in the water zone in millidarcies (mD)
reservoir_pressure = 3000  # Reservoir pressure in psi

#Pressure Drawdown 
Pressure_Drawdown = reservoir_pressure-BHP
Pressure_Drawdown_Percentage = ((reservoir_pressure-BHP)/reservoir_pressure)*100

print(Pressure_Drawdown)
print(Pressure_Drawdown_Percentage)


#Flow rate calculation 
Horizontal_Well_Flow = (0.00708*permeability*NetPay*(reservoir_pressure-BHP))/(viscosity*(math.log(well_length/well_radius)))

print(Horizontal_Well_Flow)

#Coning rate (psi) 

Critical_Pressure_Coning = ((oil_column_height*(water_density-oil_density))/(1+((water_permeability*water_column_height)/(oil_permeability*oil_column_height))))*(32.17/2)

print(Critical_Pressure_Coning)
