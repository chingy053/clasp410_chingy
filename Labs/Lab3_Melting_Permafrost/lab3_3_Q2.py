#!/usr/bin/python3

'''
This file solve Question 2 (prompt as shown below) from Lab 3 and produce the plots.

Question 2: Apply your heat equation solver to investigate permafrost in Kangerlussuaq, Greenland. Use a spatial grid that ranges from a depth of zero meters (i.e., the surface) to 100 meters below ground. Set your upper boundary condition to be a function of time using the Kangerlussuaq temperature function defined above. Set your lower boundary condition to be 5◦C, representing geothermal warming at that depth. Run your code until you reach a steady-state solution in the isothermal region (i.e., given another year, the isothermal region temperature does not change hardly at all). This will take a long time! Answer the following questions: Based on typical thermal diffusivity values for permafrost, what is the depth of the active layer and permafrost layer? With an initial condition of 0◦C, how long does it take for the ground to reach a steady state?
 
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab3_1_functions import solve_heat, plot_heatsolve, temp_kanger
#---------------------------------------------------------------

#------> Defining constants
# Convert c2 from 0.25 mm^2/s to m^2/day
c2_2 = 0.25*1E-6*60*60*24 #m^2/day
days_2 = 50*365
dt_2 = 1

#------> Solve for solutions
t_2,x_2,U_2 = solve_heat(xstop=100, tstop = days_2, dx=1, dt = dt_2, c2 = c2_2,lowerbound=temp_kanger,upperbound=5)

#------> Get summer and winter values
# Set indexing for the final year of results:
loc = int(-365/dt_2) # Final 365 days of the result.
# Extract the min values over the final year:
winter_2 = U_2[:, loc:].min(axis=1)
summer_2 = U_2[:, loc:].max(axis=1)

#------> Find the depth of active layer and permafrost layer
# Find index for depths shallower than 10 m
idx_AL = np.argmin(np.abs(summer_2[x_2 < 10] - 0)) # active layer
idx_s_PL = np.argmin(np.abs(summer_2[x_2 > 10] - 0))  # permafrost layer
idx_PL = np.arange(len(x_2))[x_2 > 10][idx_s_PL]    # index in full array

print(f"The active layer is about {x_2[idx_AL]:.2f} m in depth, beneath which the permafrost layer extends down to approximately {x_2[idx_PL]:.2f} m.")

#------> Plot
fig1, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 7))
plt.style.use('fivethirtyeight')
contour_2 = ax1.pcolor(t_2/365, x_2, U_2,cmap='seismic',vmin=-25,vmax=25)
cbar_2 = plt.colorbar(contour_2)
cbar_2.set_label(r'Temperature ($^{\circ}C$)')
ax1.set_title("Ground Temperature at Kangerlussuaq, Greenland")
ax1.set_xlabel("Time ($years$)")
ax1.set_ylabel("Depth ($m$)")
ax1.invert_yaxis()

ax2.plot(summer_2, x_2, 'r')
ax2.plot(winter_2, x_2, 'b')
ax2.set_title("Ground Temperature at Kangerlussuaq, Greenland")
ax2.axvline(x=0, color='k', linestyle='--', linewidth=2)
ax2.set_xlim(-15,10)
ax2.set_ylim(-5,60)
ax2.set_xlabel("Temperature ($°C$)")
ax2.set_ylabel("Depth ($m$)")
ax2.annotate(f"{x_2[idx_AL]:.2f} m", xy=(0, x_2[idx_AL]), xytext=(2, x_2[idx_AL]+3), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax2.annotate(f"{x_2[idx_PL]:.2f} m", xy=(0, x_2[idx_PL]), xytext=(2, x_2[idx_PL]+3), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax2.invert_yaxis()
plt.tight_layout()
plt.savefig("plot_lab3_3_Q2.png")
plt.close()