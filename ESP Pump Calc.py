# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:38:29 2023

@author: AHernandez
"""

#Step 1: Basic Well Information 

Casing = 7  #inches 26# 
Tubing = 3.5  #inches 9.2# N80 BU
Top_Perforations = 2003  #meters 
Pump_Intake_Depth = 1713  #meters 
Oil_Gravity = 35 #API 
Water_Cut = 0.90 #Percentage 
Water_Gravity = 1.01 
Gas_Gravity = 0.8 
Producing_GOR = 200 #scf/stb 
Reservoir_Pb = 964  #psi 
Bottomhole_Temperature = 90 #degC 
Wellhead_Temperature = 50  #degC 
Flowing_Wellhead_Pressure = 87 #psi
Static_Pressure = 2320.6 #psi
Casing_Head_Pressure = 16 #psi 
Production_Rate = 2500 #bfpd 
Pump_Intake_Pressure = 1160 #psi
Datum_Point = 2003 #meters Top of Perforations 
Desired_Production_Rate = 3500 #bfpd WANT PRODUCTION RATE 
Available_Primary_Voltage = 419 #V 
Desired_Frequency_Range = 40 #Hz
Desired_Frequency_Range_2 = 65  #Hz
Motor_Temperature = 70 + 88 #88 is conversion factor of 70 degC to F
Gas_Comp_Factor = 0.875
C_Constant = 120      #For Tubing Friction Calcs 
ID = 2.992  #inches of tubing 3.5" 9.2# N80
Head_Pump_per_Stage_Conversion = 0.0024  #multiply bfpd by this value to get it in m then multiply by 3.28 to convert it to ft 


#Possible Problems? 
#- No sand production, no scale deposits 
#- No gas impurities (N2, H2S and Co2)

#Step 2: Production Capacity
Specific_Gravity_Oil = (141.5)/(Oil_Gravity + 131.5)
Specific_Gravity_Water_Mixture = (Water_Cut)*Water_Gravity+(1-Water_Cut)*Specific_Gravity_Oil
Well_Flowing_Pressure = (Pump_Intake_Pressure)+0.433*Specific_Gravity_Water_Mixture*(Datum_Point-Pump_Intake_Depth)*3.28
Productivity_Index = (Production_Rate)/(Static_Pressure-Well_Flowing_Pressure)
#Calculate Pwf at desired production rate 
Well_Flowing_Pressure_Desired_Rate = Static_Pressure-Desired_Production_Rate/Productivity_Index
Pump_Intake_Pressure_at_Desired_Rate = Well_Flowing_Pressure_Desired_Rate-(Well_Flowing_Pressure-Pump_Intake_Pressure)

if Pump_Intake_Pressure_at_Desired_Rate < Reservoir_Pb: 
    
    Solution_Gas_Ratio = Gas_Gravity*((Pump_Intake_Pressure_at_Desired_Rate*10**(0.0125*Oil_Gravity))/(18*10**(0.00091*Motor_Temperature)))**1.20482
    Oil_Formation_Volume_Factor = 0.972+0.000147*(Solution_Gas_Ratio*(Gas_Gravity/Solution_Gas_Ratio)**0.5 + 1.25*Motor_Temperature)**1.175
    Gas_Formation_Volume_Factor = (5.05*0.875*(Motor_Temperature+460))/Pump_Intake_Pressure_at_Desired_Rate
    Total_Gas_Volume = (Producing_GOR*Desired_Production_Rate*(1-Water_Cut))/1000
    Solution_Gas_Volume = (Solution_Gas_Ratio*Desired_Production_Rate*(1-Water_Cut))/1000
    Free_Gas_Volume = Total_Gas_Volume-Solution_Gas_Volume
    
    Volume_Oil_Pump_Intake = Oil_Formation_Volume_Factor*Desired_Production_Rate*(1-Water_Cut)
    Volume_Gas_Pump_Intake = Free_Gas_Volume*Gas_Formation_Volume_Factor
    Volume_Water_Pump_Intake = Desired_Production_Rate*Water_Cut
    Total_Fluid_Volume_Pump_Intake = Volume_Gas_Pump_Intake+Volume_Oil_Pump_Intake+Volume_Water_Pump_Intake
    
    Percentage_Free_Gas = (Volume_Gas_Pump_Intake/Total_Fluid_Volume_Pump_Intake)*100
    
    Total_Mass_Fluid_Produced = ((Desired_Production_Rate*(1-Water_Cut)*Specific_Gravity_Oil)+(Desired_Production_Rate*Water_Cut*Water_Gravity))+5.6145*62.4*(Producing_GOR*Desired_Production_Rate*(1-Water_Cut)*Gas_Gravity*0.0752)
    Composite_Specific_Gravity = (Total_Mass_Fluid_Produced)/(Desired_Production_Rate*5.6146*62.4)
    
else:
        print("Fluid rate oil with free gas")
    
#Total Pump Dynamic Head = HL(Pump Depth) + Ft(Tubing Friction Loss) + Hwh(Wellhead Pressure Head)
    
#Net Well Lift Calculation 
Pump_Intake_Pressure_at_Desired_Rate_HeightofFluid = (Pump_Intake_Pressure_at_Desired_Rate)/(0.433*Composite_Specific_Gravity)
HL = (Pump_Intake_Depth*3.28)-Pump_Intake_Pressure_at_Desired_Rate_HeightofFluid

#Tubing Friction Lss Calculation 
Friction_Lss_Factor = ((15.11*(Desired_Production_Rate/C_Constant)**1.852)/(ID**4.8655))
Tubing_Friction_Loss = Friction_Lss_Factor*((Pump_Intake_Depth*3.28)/1000)      #in ft

#Wellhead Pressure 
Hwh = Flowing_Wellhead_Pressure/(0.433*Composite_Specific_Gravity)

Total_Dynamic_Head = HL + Hwh + Tubing_Friction_Loss

Head_per_Stage = Desired_Production_Rate*Head_Pump_per_Stage_Conversion
Pump_Stages = Desired_Production_Rate/(Head_per_Stage*3.28)

print(Total_Dynamic_Head)
print(Head_per_Stage)
print(Pump_Stages)





                                            




































