#!/usr/bin/python3
'''
Solve the diffusion problem to learn how to drink coffee effectively
Tell Sara how to run your code
'''

import numpy as np
import matplotlib.pyplot as plt 

def solve_heat(xstop=1, tstop = 0.2, dx=0.2, dt=0.02, c2=1, bc_type="dirichlet"):
    '''
    A function for solving the heating equation

    Parameter
    --------------
    Fill this out don't forget. :P

    Returns
    --------------
    x, t: 1D Numpy arrays
        Space and time values, respectively
    
    U : Numpy array
        Theh solution of the heat equation, size is nSpace x nTime
    '''
    #Check our stability criterion:
    dt_max = dt>dx**2/(2*c2)
    #if dt>dt_max:
    #    raise ValueError(f'DANGER:dt = {dt} > dt_max={dt_max}.')

    # Get grid sizes (plus one to include "0" as well)
    N = int(tstop/dt)+1
    M = int(xstop/dx)+1
    if abs(tstop % dt) > 1e-12:
        raise ValueError('Non-even')
    
    # Set up space and time grid
    t = np.linspace(0, tstop, N)
    x = np.linspace(0, xstop, M)

    # Create solution matrix; set initial condition
    U = np.zeros([M, N])
    U[:,0] = 4*x-4*x**2

    # Get r
    r = c2*(dt/dx**2)

    # Solve our equation
    for j in range(N-1):
        U[1:M-1, j+1] = (1-2*r)*U[1:M-1,j] + r*(U[2:M,j]+U[:M-2,j])
        if bc_type == "neumann":
            # Neumann boundary condition: enforce dU/dx = 0 at boundaries
            U[0, j+1]  = U[1, j+1]
            U[-1, j+1] = U[-2, j+1]
        elif bc_type == "dirichlet":
            # Dirichlet boundary condition: enforce U = 0 at boundaries
            # Our code already implicitly keeps U[0,*] and U[-1,*] = 0
            pass
    
    # Return our pretty solution to the caller
    return t,x,U

def plot_heatsolve(t,x,U,title=None, cmap = 'inferno', fig=None, ax=None,**kwargs):
    '''
    plot the 2D solutions 

    Parameter
    --------------
    x, t: 1D Numpy arrays
        Space and time values, respectively
    
    U : Numpy array
        Theh solution of the heat equation, size is nSpace x nTime

    Return
    --------------
    fig,ax : Matplotlib figure & axes objects,
        The figure and axes of the plot.
    
    cbar : Matplotlib color object
        The color bar on the final plot
    '''
    plt.style.use('fivethirtyeight')

    # Check our kwargs for defaults:
    # Set default cmap to inferno
    if 'cmap' not in kwargs:
        kwargs['cmap'] = 'inferno'

    # Create and configure figure & axes:
    fig, ax = plt.subplots(1,1, figsize = (8,6))

    # Add contour to our axes:
    contour = ax.pcolor(t,x,U,**kwargs,cmap=cmap)
    cbar = plt.colorbar(contour)

    # Add labels to stuff!
    cbar.set_label(r'Temperature ($^{\circ}C$)')
    ax.set_xlabel('Time ($s$)')
    ax.set_ylabel('Position ($m$)')
    ax.set_title(title)
    fig.tight_layout()

    return fig, ax, cbar

# Default setting
#t_test,x_test,U_test = solve_heat()
#fig, ax, cbar = plot_heatsolve(t=t_test,x=x_test,U=U_test,title="Default Test")

# Using both Dirichlet and Neumann Cases with dx = 0.02
t_002,x_002,U_D = solve_heat(dx=0.02,dt = 0.0002, bc_type="dirichlet")
t_002,x_002,U_N = solve_heat(dx=0.02,dt = 0.0002, bc_type="neumann")

fig1, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 7))
contour1_D = ax1.pcolor(t_002, x_002, U_D, cmap='inferno')
ax1.set_title("Dirichlet Boundary Condition")
ax1.set_xlabel("Time ($s$)")
ax1.set_ylabel("Position ($m$)")

contour1_N = ax2.pcolor(t_002, x_002, U_N, cmap='inferno')
ax2.set_title("Neumann Boundary Condition")
ax2.set_xlabel("Time ($s$)")
ax2.set_ylabel("Position ($m$)")

cbar = fig1.colorbar(contour1_N, ax=[ax1, ax2], location="right")
cbar.set_label(r'Temperature ($^{\circ}C$)')
fig1.suptitle("Heat Equation Solutions with Different Boundary Conditions (dx=0.02,dt=0.0002)",fontsize=20, x=0.45)
plt.rcParams.update({'font.size': 16})
plt.savefig("plot_lec4_hw.png")

