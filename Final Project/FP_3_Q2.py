#!/usr/bin/python3
'''
This code is used to solve Problem 2 from the freeze of liquid droplet problem.

2.	Perform a sensitivity analysis by varying the droplet radius from 0.1 µm to 70 µm and the thermal diffusivity from 1.5 to 3.0. How do these changes affect the total time required for the droplet to solidify?
'''

import numpy as np
import matplotlib.pyplot as plt 
from FP_1_functions import solve_freeze

plt.style.use('fivethirtyeight')

#---------> Varying the radius
# radius_ = np.arange(10e-6, 71e-6, 10e-6)
# radius_list = np.insert(radius_, 0, 0.1 * 1e-6)

# fig, ax = plt.subplots(figsize=(16, 10))
# for jj in range(len(radius_list)):
#     [t_21,x_21,U_21,s_21,r_i_21,_,_,t_phys_21, x_phys_21, _]=solve_freeze(R=radius_list[jj])

#     # Convert to microns for legend
#     radius_um = radius_list[jj] * 1e6

#     # Convert to microns for yaxis
#     r_i_um = r_i_21 * 1e6

#     # Plot
#     ax.plot(t_phys_21, r_i_um, linewidth=2,
#             label=f"R = {radius_um:.1f} µm")
#     ax.set_xlabel("Time (s)")
#     ax.set_ylabel("Freezing Front Radius (µm)")
#     ax.set_title("Freezing Front Propagation with Varying Droplet Sizes")
# ax.legend()
# fig.tight_layout()
# plt.rcParams.update({'font.size': 20})
# fig.savefig("plot_FP_3_Q2_f1.png")


#---------> Varying the thermal conductivity
k_list = np.arange(1.5, 3.0 + 0.5, 0.5)

fig1, ax1 = plt.subplots(figsize=(16, 10))

for kk in range(len(k_list)):
    [t_22, x_22, U_22, s_22, r_i_22, _, _, t_phys_22, x_phys_22, _] = solve_freeze(k_s=k_list[kk])

    # Convert freezing front radius to microns for plotting
    r_i_um = r_i_22 * 1e6

    ax1.plot(t_phys_22, r_i_um, linewidth=2,
            label=f"Thermal Conductivity = {k_list[kk]:.2f} W/m/K")

ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Freezing Front Radius (µm)")
ax1.set_title("Freezing Front Propagation with Varying Thermal Conductivity")
ax1.legend()
fig1.tight_layout()
plt.rcParams.update({'font.size': 20})
fig1.savefig("plot_FP_3_Q2_f2.png")