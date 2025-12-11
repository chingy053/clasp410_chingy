#!/usr/bin/python3
'''
This code is used to validate the freeze of liquid droplet solver.

1.	Write a function that solves the heat equation using specified initial conditions and boundary conditions. Make reasonable choices for the spatial and temporal domains and step sizes. The function should return three outputs of the spatial grid, the time grid, and a 2-D array of the temperature field. Verify your solution by comparing it with Figure 1.
'''

import numpy as np
import matplotlib.pyplot as plt 
from FP_1_functions import solve_freeze

plt.style.use('fivethirtyeight')

[t_1,x_1,U_1,s_1,r_i_1,du_dx_1, ds_dt_1,t_phys_1, x_phys_1, t_char_1]=solve_freeze(R=2e-5)

# --------------> Plot 1: t vs r_i
# similar to Fig 12 from Feuillebois et al. (1995)
r_i_cm = r_i_1 * 100.0        # m to cm
t_s    = t_phys_1             # s

fig, ax = plt.subplots(figsize=(16, 10))
ax.plot(t_s, r_i_cm, linewidth=2)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Freezing Front Radius (cm)")
ax.set_title("How long does it take for the freezing front to propagate?")
fig.tight_layout()
plt.rcParams.update({'font.size': 20})
fig.savefig("plot_FP_2_validate_f1.png")

# --------------> Plot 2: heatmap
fig1, ax1 = plt.subplots(figsize=(16, 10))
im = ax1.imshow(
    U_1.T,
    extent=[x_phys_1[0], x_phys_1[-1], t_phys_1[0], t_phys_1[-1]],
    aspect="auto",
    origin="lower"
)
cbar = fig1.colorbar(im, ax=ax1)
cbar.set_label("U(x,t)")
ax1.set_xlabel("Radius (m)")
ax1.set_ylabel("Time (s)")
ax1.set_title("Space–Time Evolution of U(x,t) (20 µm Droplet)")
fig1.tight_layout()
plt.rcParams.update({'font.size': 20})
fig1.savefig("plot_FP_2_validate_f2.png")
