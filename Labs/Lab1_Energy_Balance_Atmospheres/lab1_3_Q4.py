#!/usr/bin/python3
'''
This file solve Question 4 (prompt as shown below) from Lab 1 and produce the plots.

Question 4: How many atmospheric layers do we expect on the planet Venus? Although the Earth has greenhouse gases, Venus currently exhibits a much stronger Greenhouse effect. We know that the surface temperature of Venus is ∼ 700K and typical solar flux, S0, is 2600 W/m2. Assume that Venus has N atmospheric layers where N > 1. Assume that each layer of the atmosphere is transparent to short wave radiation, but absorbs all long wave energy incident upon it (i.e., ε = 1). How many perfectly absorbing layers do you need to match the surface temperature of Venus?

Plot : Altitude versus temperature to produce an altitude profile of the modeled system
'''
#---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from lab1_1_nlayer import n_layer_atmos, Stefan_Boltzmann

#---------------------------------------------------------------
# 4: Run the model for Venus
#    Assume the following for Venus:
#    - Surface y = ∼ 700K
#    - S0 = 2600 W/m2
#    - N atmospheric layers where N > 1
#    - Emissivity = 1
#---------------------------------------------------------------

#---------> Calculate the temperature for each layer and plot

# Define the number of layers
n_4 = np.linspace(2,151,150)
temp_4 = np.zeros(len(n_4))

# Loop through each layer
fig3, ax3 = plt.subplots(figsize=(16,10))

for kk in range(len(n_4)):

    # Get vertical temperature profile
    temp_4[kk] = Stefan_Boltzmann(n_layer_atmos(int(n_4[kk]), epsilon=1,albedo=0.8,s0=2600, debug = False))[0]

#---------> Plot!
ax3.plot(temp_4, n_4, color='b', linewidth=2)
ax3.axvline(x=700, color='k', linestyle='--')
ax3.set_xlabel('Temperature (K)')
ax3.set_ylabel('Number of Layers')
ax3.set_title(f'How many perfectly absorbing layers would give Venus a surface temperature of 700 K?')
ax3.text(380, 148, "Solar Irradiance = 2600 W/m$^{2}$, Albedo = 0.8, Emissivity = 1", fontsize=16, color="k")
ax3.grid(True)
plt.rcParams.update({'font.size': 16})
fig3.savefig("plot_lab1_3_Q4.png")
fig3.show()

#---------> Print the statement
n_at_700 = n_4[np.argmin(np.abs(temp_4 - 700))]
print(f'The model predicts that {n_at_700:.0f} perfectly absorbing atmospheric layers are needed for Venus to have a surface temperature of 700 K.')