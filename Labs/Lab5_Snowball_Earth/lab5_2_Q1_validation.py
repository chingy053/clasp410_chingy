#!/usr/bin/env python3

'''
This file solve Question 1 (prompt as shown below) from Lab 5 Snowball Earth to verify the functions.

Question 1: 
Code up the solver shown in Equation 4. Do this in parts: begin with only the basic diffusion solver (Equation 2). Use the values given in Table 1 and try to reproduce the red line in Figure 1. For this part, use an albedo of 0.3 at all points on your grid. Then, add in the spherical correction term (Equation 3) and work until you can reproduce the gold line in Figure 1. Finally, include the radiative forcing term (Equation 4); work to reproduce the green line in Figure 1. Include your validation steps in your lab report.
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab5_1_functions import gen_grid, temp_warm, insolation, snowball_earth, test_functions

plt.style.use('fivethirtyeight')
#---------------------------------------------------------------
# Get warm Earth initial condition
dlat, lats = gen_grid()
temp_init = temp_warm(lats)

# Get solution after 10K years, diffusion only
lats, temp_diff = snowball_earth(albice=0.3)
lats, temp_sphe = snowball_earth(apply_spherecorr=True,albice=0.3)
lats, temp_alls = snowball_earth(apply_spherecorr=True,apply_insol=True,albice=0.3)

# Create a fancy plot
fig, ax = plt.subplots(1,1,figsize=(16, 10))
ax.plot(lats-90, temp_init, label='Initial Condition')
ax.plot(lats-90, temp_diff, label='Diffusion Only')
ax.plot(lats-90, temp_sphe, label='Diffusion + Spherical Corr.')
ax.plot(lats-90, temp_alls, label='Diffusion + Spherical Corr. + Radiative')

# Customize like those annoying insurance commericials
ax.set_title('Solution after 10,000 Years')
ax.set_ylabel(r'Temp($^{\circ}C$)')
ax.set_xlabel('Latitude')
ax.legend(loc='best')
ax.text(-80, 18, 
        "diffusivity = 100 m²/s\n"
        "emissivity = 1.0\n"
        "albedo of water/ground = 0.3\n"
        "albedo of ice/snow = 0.3\n",
         fontsize=16, color='black')
plt.rcParams.update({'font.size': 16})
plt.savefig("plot_lab5_2_Q1_validation.png")
plt.close()