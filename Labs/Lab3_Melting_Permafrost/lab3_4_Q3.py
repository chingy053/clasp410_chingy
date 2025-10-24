#!/usr/bin/python3

'''
This file solve Question 3 (prompt as shown below) from Lab 3 and produce the plots.

Question 3: Repeat the above question, but under global warming conditions. Add a uniform 0.5, 1, and 3◦C temperature shift in Kangerlussuaq’s climate curve. How does this affect the depth and thickness of the active and permafrost layers?
 
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab3_1_functions import solve_heat, plot_heatsolve, temp_kanger
#---------------------------------------------------------------

#------> Defining constants
# Convert c2 from 0.25 mm^2/s to m^2/day
c2_3 = 0.25*1E-6*60*60*24 #m^2/day
days_3 = 50*365
dt_3 = 1

#------> Solve for solutions with shifting 0.5, 1, and 3◦C
t_shifts = [0.5, 1, 3]
results = {}

for t_sh in t_shifts:
    t_, x_, U_ = solve_heat(xstop=100, tstop = days_3, dx=1, dt = dt_3, c2 = c2_3,lowerbound=lambda t: temp_kanger(t, t_shift=t_sh),upperbound=5)

    #------> Get summer and winter values
    # Set indexing for the final year of results:
    loc = int(-365/dt_3) # Final 365 days of the result.
    # Extract the min values over the final year:
    summer = U_[:, loc:].max(axis=1)
    winter = U_[:, loc:].min(axis=1)

    #------> Find the depth of active layer and permafrost layer
    # Find index for depths shallower than 10 m
    idx_AL = np.argmin(np.abs(summer[x_ < 10] - 0))
    idx_s_PL = np.argmin(np.abs(summer[x_ > 10] - 0))
    idx_PL = np.arange(len(x_))[x_ > 10][idx_s_PL]

    #------> Store results
    results[t_sh] = (x_[idx_AL], x_[idx_PL])

    #------> Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    plt.style.use('fivethirtyeight')

    # --- Left panel: 2D temperature evolution
    contour = ax1.pcolor(t_ / 365, x_, U_, cmap='seismic', vmin=-25, vmax=25)
    cbar = plt.colorbar(contour, ax=ax1)
    cbar.set_label(r'Temperature ($^{\circ}$C)')
    ax1.set_title(f"Ground Temperature at Kangerlussuaq (T+{t_sh}°C)")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Depth (m)")
    ax1.invert_yaxis()

    # --- Right panel: Summer & Winter profiles
    ax2.plot(summer, x_, 'r', label='Summer')
    ax2.plot(winter, x_, 'b', label='Winter')
    ax2.axvline(x=0, color='k', linestyle='--', linewidth=2)
    ax2.set_xlim(-15, 10)
    ax2.set_ylim(-5, 60)
    ax2.invert_yaxis()
    ax2.annotate(f"{x_[idx_AL]:.2f} m", xy=(0, x_[idx_AL]), xytext=(2, x_[idx_AL]+3), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax2.annotate(f"{x_[idx_PL]:.2f} m", xy=(0, x_[idx_PL]), xytext=(2, x_[idx_PL]+3), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax2.set_xlabel("Temperature (°C)")
    ax2.set_ylabel("Depth (m)")
    ax2.set_title(f"Temperature Profiles (T+{t_sh}°C)")
    ax2.legend()

    # Save each figure
    plt.tight_layout()
    plt.savefig(f"plot_lab3_4_Q3_shift_{t_sh:.1f}C.png")
    plt.close()

# Print summaries
for t_shh, (d_AL, d_PL) in results.items():
    print(f"If the temperature is warmer by {t_shh}°C, the active layer is about {d_AL:.2f} m in depth, beneath which the permafrost layer extends down to approximately {d_PL:.2f} m.")