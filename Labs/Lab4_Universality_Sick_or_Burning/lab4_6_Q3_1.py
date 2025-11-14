#!/usr/bin/env python3

'''
This file solve Question 3 (prompt as shown below) from Lab 4 and produce the plots.

Question 3: 
Crack virologist ACE ZERBLONSKI is studying a new disease, Buckeyeitis. Late-stage symptoms include large red lacerations with gray dots and poor judgement concerning football teams. Use your wildfire model to investigate potential spread of this new, heinous
disease by redefining the status values above: ”2” is a healthy person, ”3” is a sick person, and ”1” is someone who has had the disease, but survived and is now immune. Introduce a new status, ”0”, to indicate persons who did not survive the infection (e.g., they went to the great programming course in the sky). Include a new variable, Pfatal, that sets the chance that infected kick it. Use Pbare to create an initial immune population thanks to a new break-through vaccine, G0-Blu3. Using this updated model, quantitatively explore the impact of different variables on the spread of the disease. Answer the question, How does disease mortality rate (Psurvive) and early vaccine rates affect disease spread?
'''
#---------------------------------------------------------------
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation, PillowWriter
from lab4_1_functions import forest_fire
#---------------------------------------------------------------

#-----------------First experiment: varying Pspread-----------------
# Setups:
# 1) Grid: 100x100
# 2) Pspread: vary
# 3) Pignite: 5%
# 4) Pbare: 5%
# 5) Pfetal: 5%
# 6) Timesteps: 40

#------> Defining a range of pspread
list_pspread = np.arange(0,1.0,0.05)
full_burn_time_3 = np.zeros(len(list_pspread))

#------> Create plots
fig, axes = plt.subplots(2,4,figsize=(16, 10))
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = axes.flatten()
for idx, ii in enumerate(list_pspread):
    # Run the model
    forest_3, full_burn_time_3[idx] = forest_fire(isize=100, jsize=100, nstep=40, case='disease' ,pspread=ii, pignite=0.05, pbare=0.05, pfetal=0.05)

    # Get the shape
    ksize, isize, jsize = forest_3.shape
    npoints = isize * jsize
    time = np.arange(ksize)

    # Calculate percentages for each category
    perc_deceased = 100 * np.sum(forest_3 == 0, axis=(1, 2)) / npoints
    perc_immune = 100 * np.sum(forest_3 == 1, axis=(1, 2)) / npoints
    perc_healthy = 100 * np.sum(forest_3 == 2, axis=(1, 2)) / npoints
    perc_sick = 100 * np.sum(forest_3 == 3, axis=(1, 2)) / npoints
    
    # Define colormap
    cmap = cm.get_cmap("jet", len(list_pspread))

    # Plot
    ax1.plot(perc_deceased,color=cmap(ii))
    ax1.set_ylabel("Percentage of Total Population")
    ax2.plot(perc_immune,color=cmap(ii))
    ax3.plot(perc_healthy,color=cmap(ii))
    ax4.plot(perc_sick,color=cmap(ii))
ax5.plot(list_pspread,full_burn_time_3,color='k',linewidth=2)

# Axis titles and labels
ax1.set_title("Deceased (%)")
ax2.set_title("Immune (%)")
ax3.set_title("Healthy (%)")
ax4.set_title("Sick (%)")
ax5.set_title("Time of Containment")
ax5.set_xlabel("Probability of Spread")
ax5.set_ylabel("Time Steps")
ax5.grid(True, linestyle="--", alpha=0.5)
ax5.set_box_aspect(1)
ax6.axis('off')
ax7.axis('off')
ax8.axis('off')

# For top 4 panels
for ax in (ax1, ax2, ax3, ax4):
    ax.set_xlabel("Time Steps")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_box_aspect(1)

# Move top 4 panels down a little
plt.subplots_adjust(hspace=0.4, top=0.8)

# Add subtitles
fig.suptitle(
    "Disease Spread Progression with Different Spread Probability\n \
        Probability of initial immune population (vaccinated) = 0.05\n \
        Probability of initial infection = 0.05\n \
        Probability of death = 0.05",
    fontsize=20, y=0.97, ha='center')

# Create one shared colorbar at the bottom middle
cbar_ax = fig.add_axes([0.35, 0.4, 0.5, 0.03])
cbar = fig.colorbar(cm.ScalarMappable(cmap=cmap),
                    ax=[ax1, ax2, ax3, ax4],
                    orientation='horizontal',
                    cax=cbar_ax)
cbar.set_label("Probability of Spread")
plt.rcParams.update({'font.size': 16})
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("plot_lab4_6_Q3_f1_varying_pspread.png")
plt.close()


#-----------------Second experiment: varying Pbare-----------------
# Setups:
# 1) Grid: 100x100
# 2) Pspread: 65%
# 3) Pignite: 5%
# 4) Pbare: vary
# 5) Pfetal: 5%
# 6) Timesteps: 40

#------> Defining a range of pbare
list_pbare = np.arange(0,1.0,0.05)
full_burn_time_33 = np.zeros(len(list_pbare))

#------> Create plots
fig, axes = plt.subplots(2,4,figsize=(16, 10))
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = axes.flatten()
for idx, ii in enumerate(list_pbare):
    # Run the model
    forest_3, full_burn_time_3[idx] = forest_fire(isize=100, jsize=100, nstep=40, case='disease' ,pspread=0.65, pignite=0.05, pbare=ii, pfetal=0.05)

    # Get the shape
    ksize, isize, jsize = forest_3.shape
    npoints = isize * jsize
    time = np.arange(ksize)

    # Calculate percentages for each category
    perc_deceased = 100 * np.sum(forest_3 == 0, axis=(1, 2)) / npoints
    perc_immune = 100 * np.sum(forest_3 == 1, axis=(1, 2)) / npoints
    perc_healthy = 100 * np.sum(forest_3 == 2, axis=(1, 2)) / npoints
    perc_sick = 100 * np.sum(forest_3 == 3, axis=(1, 2)) / npoints
    
    # Define colormap
    cmap = cm.get_cmap("jet", len(list_pbare))

    # Plot
    ax1.plot(perc_deceased,color=cmap(ii))
    ax1.set_ylabel("Percentage of Total Population")
    ax2.plot(perc_immune,color=cmap(ii))
    ax3.plot(perc_healthy,color=cmap(ii))
    ax4.plot(perc_sick,color=cmap(ii))
ax5.plot(list_pspread,full_burn_time_3,color='k',linewidth=2)

# Axis titles and labels
ax1.set_title("Deceased (%)")
ax2.set_title("Immune (%)")
ax3.set_title("Healthy (%)")
ax4.set_title("Sick (%)")
ax5.set_title("Time of Containment")
ax5.set_xlabel("Probability of Initial Immunity due to Vaccination")
ax5.set_ylabel("Time Steps")
ax5.grid(True, linestyle="--", alpha=0.5)
ax5.set_box_aspect(1)
ax6.axis('off')
ax7.axis('off')
ax8.axis('off')

# For top 4 panels
for ax in (ax1, ax2, ax3, ax4):
    ax.set_xlabel("Time Steps")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_box_aspect(1)

# Move top 4 panels down a little
plt.subplots_adjust(hspace=0.4, top=0.8)

# Add subtitles
fig.suptitle(
    "Disease Spread Progression with Different Immunity Probability\n \
        Probability of spread = 0.65\n \
        Probability of initial infection = 0.05\n \
        Probability of death = 0.05",
    fontsize=20, y=0.97, ha='center')

# Create one shared colorbar at the bottom middle
cbar_ax = fig.add_axes([0.35, 0.4, 0.5, 0.03])
cbar = fig.colorbar(cm.ScalarMappable(cmap=cmap),
                    ax=[ax1, ax2, ax3, ax4],
                    orientation='horizontal',
                    cax=cbar_ax)
cbar.set_label("Probability of Initial Immunity")
plt.rcParams.update({'font.size': 16})
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("plot_lab4_6_Q3_f2_varying_pbare.png")
plt.close()

#-----------------Third experiment: varying Pfetal-----------------
# Setups:
# 1) Grid: 100x100
# 2) Pspread: 65%
# 3) Pignite: 5%
# 4) Pbare: 5%
# 5) Pfetal: vary
# 6) Timesteps: 40

#------> Defining a range of pbare
list_pfetal = np.arange(0,1.0,0.05)
full_burn_time_333 = np.zeros(len(list_pfetal))

#------> Create plots
fig, axes = plt.subplots(2,4,figsize=(16, 10))
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = axes.flatten()
for idx, ii in enumerate(list_pfetal):
    # Run the model
    forest_3, full_burn_time_333[idx] = forest_fire(isize=100, jsize=100, nstep=40, case='disease' ,pspread=0.65, pignite=0.05, pbare=0.05, pfetal=ii)

    # Get the shape
    ksize, isize, jsize = forest_3.shape
    npoints = isize * jsize
    time = np.arange(ksize)

    # Calculate percentages for each category
    perc_deceased = 100 * np.sum(forest_3 == 0, axis=(1, 2)) / npoints
    perc_immune = 100 * np.sum(forest_3 == 1, axis=(1, 2)) / npoints
    perc_healthy = 100 * np.sum(forest_3 == 2, axis=(1, 2)) / npoints
    perc_sick = 100 * np.sum(forest_3 == 3, axis=(1, 2)) / npoints
    
    # Define colormap
    cmap = cm.get_cmap("jet", len(list_pbare))

    # Plot
    ax1.plot(perc_deceased,color=cmap(ii))
    ax1.set_ylabel("Percentage of Total Population")
    ax2.plot(perc_immune,color=cmap(ii))
    ax3.plot(perc_healthy,color=cmap(ii))
    ax4.plot(perc_sick,color=cmap(ii))
ax5.plot(list_pspread,full_burn_time_3,color='k',linewidth=2)

# Axis titles and labels
ax1.set_title("Deceased (%)")
ax2.set_title("immune (%)")
ax3.set_title("Healthy (%)")
ax4.set_title("Sick (%)")
ax5.set_title("Time of Containment")
ax5.set_xlabel("Probability of Death")
ax5.set_ylabel("Time Steps")
ax5.grid(True, linestyle="--", alpha=0.5)
ax5.set_box_aspect(1)
ax6.axis('off')
ax7.axis('off')
ax8.axis('off')

# For top 4 panels
for ax in (ax1, ax2, ax3, ax4):
    ax.set_xlabel("Time Steps")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_box_aspect(1)

# Move top 4 panels down a little
plt.subplots_adjust(hspace=0.4, top=0.8)

# Add subtitles
fig.suptitle(
    "Disease Spread Progression with Different Death Probability\n \
        Probability of spread = 0.65\n \
        Probability of initial infection = 0.05\n \
        Probability of initial immunity = 0.05",
    fontsize=20, y=0.97, ha='center')

# Create one shared colorbar at the bottom middle
cbar_ax = fig.add_axes([0.35, 0.4, 0.5, 0.03])
cbar = fig.colorbar(cm.ScalarMappable(cmap=cmap),
                    ax=[ax1, ax2, ax3, ax4],
                    orientation='horizontal',
                    cax=cbar_ax)
cbar.set_label("Probability of Death")
plt.rcParams.update({'font.size': 16})
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("plot_lab4_6_Q3_f3_varying_pfetal.png")
plt.close()