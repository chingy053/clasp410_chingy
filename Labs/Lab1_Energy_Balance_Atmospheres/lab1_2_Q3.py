#!/usr/bin/python3
'''
This file solve Question 3 (prompt as shown below) from Lab 1 and produce the plots.

Question 3: How does the surface temperature of Earth depend on emissivity and the number of layers? 
Two experiments:
  1. Using a single layer atmosphere, run your model for a range of emissivities and then plot surface temperature versus emissivity. For an average Earth surface temperature of 288K, what does your model predict for the emissivity of Earth’s atmosphere?
  2. Using this value for emissivity and vary the number of layers. How many layers of atmosphere are required to produce a surface temperature of ∼ 288K?

Plot : Altitude versus temperature to produce an altitude profile of the modeled Earth system
'''
#---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from lab1_1_nlayer import n_layer_atmos, Stefan_Boltzmann

#---------------------------------------------------------------
# 3-1: run the model for a range of emissivities and then plot surface temperature versus emissivity
#---------------------------------------------------------------

n_3_1 = 1
emit_3_1 = np.linspace(0,1,101)
temp_3_1 = np.zeros([len(emit_3_1), n_3_1+1])

#---------> Looping through the epsilons
for ii in range(len(emit_3_1)):
  temp_3_1[ii,:] = Stefan_Boltzmann(n_layer_atmos(1, epsilon=emit_3_1[ii]))

#---------> Plot surface temperature vs. emissivity
fig1, ax1 = plt.subplots(figsize=(16,10))
ax1.plot(emit_3_1,temp_3_1[:,0], color="blue", linewidth=2)
ax1.axhline(y=288, color='k', linestyle='--')
ax1.set_xlabel('Emissivity of Earth Atmopshere')
ax1.set_ylabel('Earth Surface Temperature (K)')
ax1.set_title('How does the surface temperature of Earth depend on emissivity?')
ax1.text(0.3, 298, "Solar Irradiance = 1350 W/m$^{2}$, Albedo = 0.33", fontsize=16, color="k")
ax1.grid(True)
plt.rcParams.update({'font.size': 16})
fig1.savefig("plot_lab1_2_Q3_f1.png")
fig1.show()

#---------> Find the emissivity when temperature is 288 K
temp_288 = 288
emit_at_288 = np.interp(temp_288, temp_3_1[:,0], emit_3_1)
#---------> Print the statement
print(f'For an average Earth surface temperature of 288 K, the predicted value by the model for the emissivity of Earth’s atmosphere is about {emit_at_288:.2f}.')
# plt.close()

#---------------------------------------------------------------
# 3-2: use emissivity = 0.255 and vary the number of layers.
#---------------------------------------------------------------

n_3_2 = np.linspace(1,11,11)
temp_3_2 = np.zeros(len(n_3_2))

#---------> Calculate the altitude for each layer, assuming only in the trosphere and the top of troposphere is 12km high. Evenly dividing the troposphere by the number of layer.
alt_3_2 = np.linspace(0,12,len(n_3_2)+2) *1000 # altidue in meter

#---------> Calculate the temperature for each layer and plot
fig2, ax2 = plt.subplots(figsize=(16,10))

for jj in range(len(n_3_2)): 

  # Get vertical temperature profile
  temp_3_2 = Stefan_Boltzmann(n_layer_atmos(int(n_3_2[jj]), epsilon=0.255), epsilon=0.255)

  # Define colors for plotting
  def_colors = plt.cm.rainbow(np.linspace(0, 1, len(n_3_2)))

  # Plot!
  ax2.plot(temp_3_2, alt_3_2[:jj+2], color = def_colors[jj], linewidth=2, label = f'{n_3_2[jj]:.0f} Layers')

ax2.axvline(x=288, color='k', linestyle='--')
ax2.set_xlabel('Temperature (K)')
ax2.set_ylabel('Altitude (m)')
ax2.legend()
ax2.set_title(f'Vertical Temperature Profile for {len(n_3_2)} Layers')
ax2.text(235, 11000, "Solar Irradiance = 1350 W/m$^{2}$, Albedo = 0.33, Emissivity = 0.255", fontsize=16, color="k")
ax2.grid(True)
plt.rcParams.update({'font.size': 16})
fig2.savefig("plot_lab1_2_Q3_f2.png")
fig2.show()
# plt.close()



