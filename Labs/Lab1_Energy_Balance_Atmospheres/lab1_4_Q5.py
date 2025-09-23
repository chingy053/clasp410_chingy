#!/usr/bin/python3
'''
This file solve Question 5 (prompt as shown below) from Lab 1 and produce the plots.

Question 5: A ”nuclear winter” occurs when, after a large-scale nuclear war, ash and smoke fill the atmosphere and make it opaque to short wave radiation. In terms of our model, the top-most layer of the atmosphere absorbs all incoming solar flux; none reaches the ground. Only graybody radiation warms the layers below, including the Earth's surface. Answer the science question, What would the Earth's surface temperature be under a nuclear winter scenario?. To do this, change your model so that solar flux is completely absorbed by the top layer of the atmosphere. Use 5 layers and set the emissivity to 0.5. Set S0 = 1350W/m2. What is the resulting surface temperature? Plot altitude versus temperature to produce an altitude profile of your new Earth system.

Plot : Plot altitude versus temperature for vertical profile.
'''
#---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from lab1_1_nlayer import n_layer_nuclear_winter, Stefan_Boltzmann

#---------------------------------------------------------------
# 5: Run the model for Nuclear Winter case on the Earth
#    Assume the following :
#    - S0 = 1350 W/m2, absorbed by the top of atmosphere
#    - Number of layer = 5
#    - Emissivity = 0.5
#---------------------------------------------------------------

n_5 = 5

#---------> Calculate the altitude for each layer, assuming only in the trosphere and the top of troposphere is 12km high. Evenly dividing the troposphere by the number of layer.
alt_5 = np.linspace(0,12,n_5+1) *1000 # altidue in meter

#---------> Calculate the temperature for each layer and plot
fig5, ax5 = plt.subplots(figsize=(16,10))

# Get vertical temperature profile
temp_5 = Stefan_Boltzmann(n_layer_nuclear_winter(n_5, epsilon=0.5), epsilon=0.5)

#---------> Plot!
ax5.plot(temp_5, alt_5, color = 'b', linewidth=2)
ax5.set_xlabel('Temperature (K)')
ax5.set_ylabel('Altitude (m)')
ax5.set_title(f'Vertical Temperature Profile for {n_5} Layers in Nuclear Winter Scenario')
ax5.text(255, 0, "Solar Irradiance = 1350 W/m$^{2}$, Albedo = 0.33, Absorptivity of SW at TOA = 1, Emissivity = 0.5", fontsize=16, color="k")
ax5.grid(True)
plt.rcParams.update({'font.size': 16})
fig5.savefig("plot_lab1_4_Q5_f1.png")
fig5.show()
# plt.close()

#---------> Print the statement
print(f'The model predicts that the surface temperature of the Earth would be {temp_5[0]:.2f} K in the Nuclear Winter scenario.')