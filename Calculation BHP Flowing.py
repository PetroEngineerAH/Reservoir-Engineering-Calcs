# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 07:46:07 2024

@author: ahernandez
"""

#FBHP Calculation: FBHP = P(PIP) + P(HYD)

#Calculate Hydrostatic Pressure based on Fluid gradient 

water_gradient = 0.433333  #psi/ft 

oil_gradient = 0.400       #psi/ft 

oil_production =  0   #bopd 

water_production = 0  #bwpd 

if water_production > 0:

    water_cut = (water_production)/(oil_production + water_production)
    
    fluid_gradient_mixture = (water_gradient*water_cut) + (oil_gradient*(1-water_cut))
    
    sensor_depth = 8051  #ftTVD 
    
    MPP_depth = 9816   #ftTVD 
    
    Delta_depth = MPP_depth-sensor_depth
    
    Hydrostatic_Pressure = fluid_gradient_mixture*(Delta_depth)

    # print(Hydrostatic_Pressure)
    # print (water_cut)
    # print(fluid_gradient_mixture)
    # print(Delta_depth)
    
    #Calculate Flowing bottomhole pressure 
    Pump_Intake_Pressure = 1720   #psi 
    
    #Calculate Flowing Bottomhole Pressure 
    
    BHP_Flowing = Hydrostatic_Pressure + Pump_Intake_Pressure

    print(BHP_Flowing)
    
else: 
   
    Fluid_Level = 4000      #Fluid Level in the well in ftTVD 
    
    water_gradient = 0.4333
    
    Hydrostatic_Pressure = water_gradient*Fluid_Level    #ft cancel out and have psi 
    
    BHP_Static = Hydrostatic_Pressure 

    print(BHP_Static)
    

    
 