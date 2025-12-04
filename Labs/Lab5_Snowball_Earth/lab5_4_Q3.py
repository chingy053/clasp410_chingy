#!/usr/bin/env python3

'''
This file solve Question 3 (prompt as shown below) from Lab 5 Snowball Earth.

Question 3: 
Use your function to explore how initial conditions affect the equilibrium solution. Switch from constant albedo to dynamic albedo. Begin with a ”hot” Earth (60◦ at all locations) what is your equilibrium solution? Repeat with a ”cold” Earth (-60◦ at all locations) - what is your equilibrium solution Finally, ”flash freeze” the Earth by starting with the warm Earth solution curve you used in Part 1 and 2, but now set albedo to 0.6. How do these results compare to each other? What does it tell us about the stability of snowball vs. warm Earth solutions?
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from lab5_1_functions import gen_grid, temp_warm, insolation, snowball_earth, test_functions

plt.style.use('fivethirtyeight')
#---------------------------------------------------------------

# Choosing diffusivity=80 and emissivity=0.7
lats, temp_31 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,init_cond=60.0)
lats, temp_32 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,init_cond=-60.0)
lats, temp_33 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,albgnd=0.3,albice=0.6) # (Dynamic Albedo, albedo of water = 0.3, albedo of ice = 0.6)
lats, temp_34 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,albgnd=0.3,albice=0.3) # (Constant Albedo, albedo of water = 0.3, albedo of ice = 0.3)
lats, temp_35 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,albgnd=0.6,albice=0.6) # (Constant Albedo, albedo of water = 0.6, albedo of ice = 0.6)


# Plot
fig1, ax1 = plt.subplots(1,1,figsize=(16, 10))
ax1.plot(lats-90,temp_31, "r", label=f"Hot Earth (60°C)",linewidth=3)
ax1.plot(lats-90,temp_32, "b", label=f"Cold Earth (-60°C)",linewidth=3)
ax1.plot(lats-90,temp_33, "g", label=f"Warm Earth (Dynamic Albedo)",linewidth=3)
ax1.plot(lats-90,temp_34, "k", label=f"Warm Earth (Constant Albedo = 0.3)",linewidth=3)
ax1.plot(lats-90,temp_35, "m", label=f"Warm Earth (Constant Albedo = 0.6)",linewidth=3)
ax1.legend()
ax1.set_ylabel(r'Temperature ($^{\circ}C$)')
ax1.set_xlabel('Latitude')
ax1.set_title('Latitudinal Temperature Profiles with Varying Initial Temperatures')
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.text(-85, 13, 
        "diffusivity = 80 m²/s\n"
        "emissivity = 0.7\n"
        "constant albedo = 0.3 or 0.6\n"
        "dynamic albedo (water) = 0.3\n"
        "dynamic albedo (ice) = 0.6\n",
         fontsize=16, color='black')
plt.savefig("plot_lab5_4_Q3.png")
plt.close()