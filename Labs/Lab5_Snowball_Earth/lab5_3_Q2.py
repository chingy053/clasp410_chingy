#!/usr/bin/env python3

'''
This file solve Question 2 (prompt as shown below) from Lab 5 Snowball Earth.

Question 2: 
Tune your model so that it can reproduce the warm-Earth equilibrium. There are two parameters in our model that contain much uncertainty: diffusivity (λ) and emissivity (ε). Explore each independently (allow λ to range from 0 to 150 and ε to range from 0 to 1) to determine their impact on the equilibrium solution. Then, pick a value for each that, when used in combination, allows you to best reproduce the ”warm Earth” curve given by temp_warm(). Report your findings and use these values for the rest of the lab.
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from lab5_1_functions import gen_grid, temp_warm, insolation, snowball_earth, test_functions

plt.style.use('fivethirtyeight')
#---------------------------------------------------------------
difu_range = np.linspace(0., 150., 16)
emis_range = np.linspace(0., 1., 11)

# Get warm Earth initial condition
dlat, lats = gen_grid()
temp_init = temp_warm(lats)

# --------------------> Varying Diffusivity
fig, ax = plt.subplots(1,1,figsize=(16, 10))
for ii in range(len(difu_range)):

    # Define colormap
    cmap = cm.get_cmap("jet", len(difu_range))

    lats, temp_21 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam = difu_range[ii],albice=0.3)

    # Plot
    ax.plot(lats-90,temp_21,color=cmap(ii), label=f"λ = {difu_range[ii]}")
ax.plot(lats-90, temp_init, "k" ,label='Warm Earth',linewidth=3)
ax.legend()
ax.set_ylabel(r'Temperature ($^{\circ}C$)')
ax.set_xlabel('Latitude')
ax.set_title('Latitudinal Temperature Profiles with Varying Diffusivity (λ)')
ax.grid(True, linestyle="--", alpha=0.5)
ax.text(-80, 13, 
        "emissivity = 1.0\n"
        "constant albedo = 0.3\n",
         fontsize=16, color='black')
plt.savefig("plot_lab5_3_Q2_f1_vary_diffusivity.png")
plt.close()

# --------------------> Varying Emissivity
fig2, ax2 = plt.subplots(1,1,figsize=(16, 10))
for gg in range(len(emis_range)):

    # Define colormap
    cmap = cm.get_cmap("jet", len(emis_range))

    lats, temp_22 = snowball_earth(apply_spherecorr=True,apply_insol=True,emiss = emis_range[gg],albice=0.3)

    # Plot
    ax2.plot(lats-90,temp_22,color=cmap(gg), label=f"ε = {emis_range[gg]:.1f}")
ax2.plot(lats-90, temp_init, "k" ,label='Warm Earth',linewidth=3)
ax2.legend()
ax2.set_ylabel(r'Temperature ($^{\circ}C$)')
ax2.set_xlabel('Latitude')
ax2.set_title('Latitudinal Temperature Profiles with Varying Emissivity (ε)')
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.text(-85, 390, 
        "diffusivity = 100 m²/s\n"
        "constant albedo = 0.3\n",
         fontsize=16, color='black')
plt.savefig("plot_lab5_3_Q2_f2_vary_emissivity.png")
plt.close()

# --------------------> Choose the closest value: final choice
fig5, ax5 = plt.subplots(1,1,figsize=(16, 10))

# Choosing diffusivity=80 and emissivity=0.7
lats, temp_25 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,albice=0.3)

# Plot
ax5.plot(lats-90,temp_25, "r", label=f"λ = 80.0 and ε = 0.7")
ax5.plot(lats-90, temp_init, "k" ,label='Warm Earth',linewidth=3)
ax5.legend()
ax5.set_ylabel(r'Temperature ($^{\circ}C$)')
ax5.set_xlabel('Latitude')
ax5.set_title('Latitudinal Temperature Profiles')
ax5.grid(True, linestyle="--", alpha=0.5)
ax5.text(-80, 18, 
        "diffusivity = 80 m²/s\n"
        "emissivity = 0.7\n"
        "constant albedo = 0.3\n",
         fontsize=16, color='black')
plt.savefig("plot_lab5_3_Q2_f3_choosing_difu80_emis07.png")
plt.close()