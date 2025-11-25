#!/usr/bin/python3
'''
This code is based on Feuillebois et al. (1995) Equations 14-23, solving for the freeze of liquid droplet using heat diffusion equations.
'''

import numpy as np
import matplotlib.pyplot as plt 

# def solve_freeze():
'''
A function for solving the freezing equation

Parameter
--------------

Return
--------------
'''

r_e = 75    # Final Radius (micron)
rho_s = 10  # Mass Density (??)
C_s = 10    # Specific Heat (??)
X_s = 10    # Thermal Conductivity (??)
a_s = 10    # Thermal Diffusivity (??)

# Characteristic time: for heat to diffuse across the droplet
t_star_k = r_e**2*rho_s*C_s/X_s 
#------------------------------------------------------------
#              Ignore whatever constant is above
#------------------------------------------------------------
tstop = 500
xstop = 10
dt = 1
dx = 1

# Get grid sizes (plus one to include "0" as well)
N = int(tstop/dt)+1
M = int(xstop/dx)+1

# Set up space and time grid
t = np.linspace(0, tstop, N)
x = np.linspace(0, xstop, M)

# Create solution matrix; set initial condition
U = np.zeros([M, N])
U[0,:] = 1

# Get r_def
epsilon = 0.01
r_def = epsilon*(dt/dx**2)

# Set s
s = np.zeros(N)
s[0] = 1

# Radius of the liquid droplet
R = xstop

# Freezing front radius r_i
# s = r_i / R
r_i = np.zeros(N)
r_i[0] = R

# Solve our equation
for j in range(N-1):
    # Equation [19]: Classic heat diffusion equation
    U[1:M-1, j+1] = (1-2*r_def)*U[1:M-1,j] + r_def*(U[2:M,j]+U[:M-2,j])
    
    # Get index i_s corresponding to s(t) position
    i_s = int(np.round(s[j] / dx)) # I am not sure if this is correct
    
    # Ensure i_s is within bounds
    if i_s < M - 1 and i_s > 0:
        # equation [21]: boundary condition u(s(t),t) = 0
        U[i_s, j+1] = 0
        
        # Equation [22]: du/dx|{x=s} = -s(t) * (ds(t)/dt)
        # This is Stefan condition
        # Using backward difference for spatial derivative
        du_dx = (U[i_s, j] - U[i_s-1, j]) / dx
        
        # ds_dt = -du_dx / s(t)
        if abs(s[j]) > 0:
            ds_dt = -du_dx / s[j]
        else:
            ds_dt = 0
        
        # Update s using forward Euler
        s[j+1] = s[j] + ds_dt * dt
    else:
        s[j+1] = s[j]

    # Save the freezing front radius as r_i = s * R
    r_i[j+1] = s[j+1] * R

# Plot results
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Temperature profile at different times
ax1 = axes[0, 0]
times_to_plot = [0, 100, 200, 300, 400, 500]
for time_idx in times_to_plot:
    ax1.plot(x, U[:, time_idx], label=f't = {time_idx}')
ax1.set_xlabel('x')
ax1.set_ylabel('u (Temperature)')
ax1.set_title('Temperature Profile at Different Times')
ax1.legend()
ax1.grid(True)

# Plot 2: Moving boundary s(t)
ax2 = axes[0, 1]
ax2.plot(t, s, 'b-', linewidth=2)
ax2.set_xlabel('t (Time)')
ax2.set_ylabel('s(t) (Nondimensional Position)')
ax2.set_title('Nondimensional Moving Boundary s(t)')
ax2.grid(True)

# Plot 3: Freezing front radius r_i(t)
ax3 = axes[1, 0]
ax3.plot(t, r_i, 'r-', linewidth=2)
ax3.axhline(y=R, color='k', linestyle='--', label=f'R = {R} (liquid radius)')
ax3.set_xlabel('t (Time)')
ax3.set_ylabel('r_i(t) (Freezing Front Radius)')
ax3.set_title(f'Freezing Front Radius r_i(t) = s(t) × R')
ax3.legend()
ax3.grid(True)

# Plot 4: Both s(t) and r_i(t) comparison
ax4 = axes[1, 1]
ax4_twin = ax4.twinx()
line1 = ax4.plot(t, s, 'b-', linewidth=2, label='s(t) (nondimensional)')
line2 = ax4_twin.plot(t, r_i, 'r-', linewidth=2, label='r_i(t) (dimensional)')
ax4.set_xlabel('t (Time)')
ax4.set_ylabel('s(t)', color='b')
ax4_twin.set_ylabel('r_i(t)', color='r')
ax4.set_title('Comparison: s(t) vs r_i(t)')
ax4.tick_params(axis='y', labelcolor='b')
ax4_twin.tick_params(axis='y', labelcolor='r')
ax4.grid(True)

# Combine legends
lines1, labels1 = ax4.get_legend_handles_labels()
lines2, labels2 = ax4_twin.get_legend_handles_labels()
ax4.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.tight_layout()
plt.show()