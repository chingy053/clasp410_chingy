#!/usr/bin/python3
'''
Solve the one-layer atmosphere problem from Lecture 2 homework
Assuming the atmoshere is completely opague
'''

import numpy as np
import matplotlib.pyplot as plt ; plt.ion()

def solve_T_E(alpha = 0.33, So = 1350):
    '''
    This function computes the temperature of the Earth surface
    as a function of the surface albedo and solar irradiance.

    Parameters
    --------------
    alpha: floating point, default to 0.33
        Earth surface albedo
    So: floating point or array, default to 1350 W/m2
        Solar irrandiance in W/m2

    
    Return
    --------------
    T_E: floating point
        Earth surface temperature
    '''
    sigma = 5.67e-8   # 𝜎, Stefan–Boltzmann Constant in W/m2/k4
    T_E = ((1-alpha)*So/(2*sigma))**(1./4.)

    return T_E



# -----> Create some real time series of variables
year = np.array([1900,1950,2000])       # time of year
s0_control = np.array([1365, 1365, 1365])     # time series of solar irrandiance (unchanged)
s0_change = np.array([1365, 1366.5, 1368])     # time series of solar irrandiance
t_anom = np.array([-0.4,0,0.4])             # time series of temperature anomalies

# -----> Calculate the temperature of Earth surface!
T_E_control = solve_T_E(So = s0_control)
T_E_So_change = solve_T_E(So = s0_change)
#print(T_E_control,T_E_So_change)

# -----> Calculate the temperature anomalies using year 1950
T_anamoly_control = T_E_control - T_E_control[1]
T_anamoly_So_change = T_E_So_change - T_E_So_change[1]

# -----> Plot the plots

# Subplot #1 = year vs. solar irrandiance
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 10))
ax1.plot(year,s0_control, color="black", linewidth=2, label='Constant Solar Irradiance')
ax1.plot(year,s0_change, color="red", linewidth=2, label='Change of Solar Irradiance')
ax1.legend()
#ax1.set_xlabel('Years')
ax1.set_ylabel('Solar Irradiance (W/m$^{2}$)')
ax1.set_title('Can the Increase of Solar Irradiance Account for Temperature Change?')
ax1.grid(True)

# Subplot #2 = year vs. temperature
ax2.plot(year,T_E_control, color="black", linewidth=2, label='Solar Irradiance = 1350 W/m$^{2}$')
ax2.plot(year,T_E_So_change, color="red",linewidth=2, label='Changing Solar Irradiance')
ax2.legend()
#ax2.set_xlabel('Years')
ax2.set_ylabel('Temperature (C)')
ax2.ticklabel_format(useOffset=False,style='plain', axis='y')
ax2.grid(True)

# Subplot #3 = year vs. temperature anamolies
ax3.axhline(y=0, color="black",linestyle='--', linewidth=1, label='No Anamoly')
ax3.plot(year,T_anamoly_So_change, color="red", linewidth=2, label='Changing Solar Irradiance')
ax3.plot(year,t_anom, color="blue", linewidth=2, label='Real Temperature Anamoly Given')
ax3.legend()
ax3.set_xlabel('Years')
ax3.set_ylabel('Temperature Anamoly (C)')
ax3.set_ylim(top=0.6)
ax3.grid(True)
plt.rcParams.update({'font.size': 16})
fig.show()

plt.savefig("Lec2_One_Layer_Atmo_fig1.png")