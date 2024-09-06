# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:26:48 2024

@author: AHernandez
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Reservoir parameters
HCPV_initial = 4500000.0  # Hydrocarbon pore volume in reservoir conditions (bbl)
OOIP = 4200000.0          # Original oil in place (STB)
current_production = 5000.0  # Current production rate per well (bbl/day)
injection_pressure_initial = 3000.0  # Initial reservoir pressure (psi)
injection_pressure_target = 4000.0   # Target reservoir pressure (psi)
oil_formation_volume_factor = 1.045  # Oil formation volume factor (bbl/STB)
water_formation_volume_factor = 1.0  # Water formation volume factor (bbl/bbl)

# Simulation parameters
start_date = datetime(2022, 9, 1)
end_date = datetime(2024, 6, 1)
dt = timedelta(days=1)
current_date = start_date

# Production rate increase parameters
initial_daily_production = 3000.0  # Initial production rate (bbl/day)
daily_production_increase = 150.0  # Daily increase in production rate (bbl/day)

# Calculate injection rate Q_inj to increase reservoir pressure
Q_prod = current_production * 4  # Total production rate from 4 producers
delta_pressure = injection_pressure_target - injection_pressure_initial

# Net injection rate to achieve the pressure increase
Q_inj = Q_prod + delta_pressure / (dt.days * water_formation_volume_factor)

# Initialize variables
hpvi_values = []
recovery_factor_values = []
cumulative_production = []
cumulative_water_injection = []
reservoir_pressure = []

# Initial conditions
total_oil_produced = 0.0
total_water_injected = 0.0
current_hpvi = HCPV_initial
current_reservoir_pressure = injection_pressure_initial

while current_date <= end_date:
    # Calculate hydrocarbon pore volume to date
    days_passed = (current_date - start_date).days
    hpvi = max(0, HCPV_initial - total_water_injected)  # Ensure HCPVI is non-negative
    
    # Calculate recovery factor to date
    recovery_factor = total_oil_produced / OOIP
    
    # Append values for plotting
    hpvi_values.append(hpvi)
    recovery_factor_values.append(recovery_factor)
    
    # Calculate cumulative production and cumulative water injection
    cumulative_production.append(total_oil_produced)
    cumulative_water_injection.append(total_water_injected)
    
    # Calculate reservoir pressure change due to injection and production
    delta_p = (Q_inj - 4 * Q_prod) * dt.days * water_formation_volume_factor / oil_formation_volume_factor
    current_reservoir_pressure += delta_p
    
    # Store current reservoir pressure (ensure it doesn't decrease below initial)
    if current_reservoir_pressure < injection_pressure_initial:
        current_reservoir_pressure = injection_pressure_initial
    reservoir_pressure.append(current_reservoir_pressure)
    
    # Update total oil produced and total water injected for the current day
    daily_oil_production = (initial_daily_production + days_passed * daily_production_increase) * 4 * dt.days  # 4 producers
    daily_water_injection = Q_inj * dt.days
    
    total_oil_produced += daily_oil_production
    total_water_injected += daily_water_injection
    
    # Move to the next day
    current_date += dt

# Convert dates to months for plotting
dates_monthly = np.arange(0, len(cumulative_production), 90)
date_labels = [(start_date + timedelta(days=int(d))).strftime('%Y-%m') for d in dates_monthly]

# Plotting results
plt.figure(figsize=(18, 12))

# Recovery factor vs. Hydrocarbon Pore Volume to Date
plt.subplot(2, 2, 1)
plt.plot(hpvi_values, recovery_factor_values, marker='o', linestyle='-', color='b')
plt.title('Recovery Factor vs. Hydrocarbon Pore Volume to Date')
plt.xlabel('Hydrocarbon Pore Volume Injected (HCPVI, bbl)')
plt.ylabel('Recovery Factor')
plt.grid(True)

# Cumulative Oil Production vs. Time
plt.subplot(2, 2, 2)
plt.plot(np.arange(len(cumulative_production)), cumulative_production, marker='o', linestyle='-', color='g')
plt.title('Cumulative Oil Production vs. Time')
plt.xlabel('Time (days)')
plt.ylabel('Cumulative Oil Production (bbl)')
plt.xticks(dates_monthly, date_labels, rotation=45)
plt.grid(True)

# Cumulative Water Injection vs. Time
plt.subplot(2, 2, 3)
plt.plot(np.arange(len(cumulative_water_injection)), cumulative_water_injection, marker='o', linestyle='-', color='r')
plt.title('Cumulative Water Injection vs. Time')
plt.xlabel('Time (days)')
plt.ylabel('Cumulative Water Injection (bbl)')
plt.xticks(dates_monthly, date_labels, rotation=45)
plt.grid(True)

# Reservoir Pressure vs. Time
plt.subplot(2, 2, 4)
plt.plot(np.arange(len(reservoir_pressure)), reservoir_pressure, marker='o', linestyle='-', color='purple')
plt.title('Reservoir Pressure vs. Time')
plt.xlabel('Time (days)')
plt.ylabel('Reservoir Pressure (psi)')
plt.xticks(dates_monthly, date_labels, rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
