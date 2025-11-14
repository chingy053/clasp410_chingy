#!/usr/bin/env python3

'''
This file solve Question 2 (prompt as shown below) from Lab 4 and produce the a plot for the first experiment.

Question 2: 
Answer the following science question: How does the spread of wildfire depend on the probability of spread of fire and initial forest density? To answer this run two experiments.First run a series of simulations where you vary Pspread (see the algorithm description below) from 0 to 1. Next, run a series of simulations where you vary the amount of non-forested cells from 0% to 100% using Pbare. Instead of setting the center cell on fire, use Pignite to set several sets of cells on fire during initialization. Set Pignite to something that is reasonable- the fire starts reliably but does not overwhelm the forest immediately. For each case, quantitatively explore the impact on wildfire evolution. What observables will you need to explore? How will you quantify and visualize the results?
'''
#---------------------------------------------------------------
import os
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation, PillowWriter
from lab4_1_functions import forest_fire
#---------------------------------------------------------------

#-----------------First experiment: varying Pspread-------------
# Setups:
# 1) Grid: 100x100
# 2) Pspread: vary
# 3) Pignite: 5%
# 4) Pbare: 0%
# 5) Pfetal: N/A
# 6) Timesteps: 40

#------> Defining a range of pspread
list_pspread = np.arange(0,1.0,0.05)
full_burn_time_2 = np.zeros(len(list_pspread))

#------> Create plots
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(16, 10))
for idx, ii in enumerate(list_pspread):
    # Run the model
    forest_2, full_burn_time_2[idx] = forest_fire(isize=100, jsize=100, nstep=40, pspread=ii, pignite=0.05, pbare=0)

    # Get the shape
    ksize, isize, jsize = forest_2.shape
    npoints = isize * jsize
    time = np.arange(ksize)

    # Calculate percentages for each category
    perc_burnt = 100 * np.sum(forest_2 == 1, axis=(1, 2)) / npoints
    perc_forest = 100 * np.sum(forest_2 == 2, axis=(1, 2)) / npoints
    perc_burning = 100 * np.sum(forest_2 == 3, axis=(1, 2)) / npoints
    
    # Define colormap
    cmap = cm.get_cmap("jet", len(list_pspread))

    # Plot
    ax1.plot(perc_burnt,color=cmap(ii))
    ax1.set_ylabel("Percentage of Total Area")
    ax2.plot(perc_forest,color=cmap(ii))
    ax3.plot(perc_burning,color=cmap(ii))
ax4.plot(list_pspread,full_burn_time_2,color='k',linewidth=2)

# Axis titles and labels
ax1.set_title("Burnt Area (%)")
ax2.set_title("Forested Area (%)")
ax3.set_title("Burning Area (%)")
ax4.set_title("Time of Containment")
ax4.set_xlabel("Probability of Spread")
ax4.set_ylabel("Time Steps")
ax4.grid(True, linestyle="--", alpha=0.5)
ax4.set_box_aspect(1)

# Get current position of ax4
pos = ax4.get_position()
# Move ax4 slightly to the right
ax4.set_position([pos.x0 + 0.03, pos.y0, pos.width, pos.height])

for ax in (ax1, ax2, ax3):
    ax.set_xlabel("Time Steps")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_box_aspect(1)

fig.suptitle(
    "Forest Fire Spread Progression with Different Spread Probability\n \
        Probability of Initial Ignite = 0.05\n \
        Probability of Initial Bare Land = 0",
    fontsize=20, y=0.825, ha='center')

# Create one shared colorbar at the bottom middle
cbar_ax = fig.add_axes([0.25, 0.2, 0.5, 0.03])
cbar = fig.colorbar(cm.ScalarMappable(cmap=cmap),
                    ax=[ax1, ax2, ax3],
                    orientation='horizontal',
                    cax=cbar_ax)
cbar.set_label("Probability of Spread")
plt.rcParams.update({'font.size': 16})
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("plot_lab4_4_Q2_f1_varying_pspread.png")
plt.close()
