#!/usr/bin/python3
'''
Solve the melting permafrost problem
'''

import numpy as np
import matplotlib.pyplot as plt 

def solve_heat(xstop, tstop, dx, dt, c2, lowerbound = 0, upperbound = 0, set_ic = None):
    '''
    A function for solving the heating equation

    Parameter
    --------------
    xstop: int
        Distance of heating in meter. 
    tstop: int
        Time of heating in day. 
    dx: int
        Distance step size in meter.
    dt: int
        Time step size in day.
    c2: int
        Thermal diffusivity in m^2/day.
    lowerbound: int or function
        Setting lower boundary condition of temperature in degree. Default is 0.
    upperbound: int or function
        Setting upper boundary condition of temperature in degree. Default is 0.
    set_ic: string
        Setting the initial condition. 
        'None': Default is None (same as Kangerlussuaq case), where it is all 0s. 
        'validation': for validation case, that is 4*x-4*x**2.
    
    Returns
    --------------
    x, t: 1D Numpy arrays
        Space and time values, respectively.
    
    U : Numpy array
        Theh solution of the heat equation, size is nSpace x nTime
    '''
    #Check our stability criterion:
    dt_max = dx**2 / (2*c2)
    if dt>dt_max:
       raise ValueError(f'DANGER:dt = {dt} > dt_max={dt_max}.')

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
    if set_ic is None:
        U = np.zeros((M,N))
    elif set_ic == 'validation':
        U[:,0] = 4*x-4*x**2

    # Get r
    r = c2*(dt/dx**2)

    # Solve our equation
    for j in range(N-1):
        U[1:M-1, j+1] = (1-2*r)*U[1:M-1,j] + r*(U[2:M,j]+U[:M-2,j])
        
        if lowerbound is None: #Neumann
            U[0, j+1] = U[1, j+1]
        elif callable(lowerbound):  # is lowerbound a function?
            U[0, j+1] = lowerbound(t[j+1])
        else: #Dirichlet/constant
            U[0, j+1] = lowerbound

        if upperbound is None: #Neumann
            U[-1, j+1] = U[-2, j+1]
        elif callable(upperbound):  # is upperbound a function?
            U[-1, j+1] = upperbound(t[j+1])
        else: #Dirichlet/constant
            U[-1, j+1] = upperbound
    
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
        The solution of the heat equation, size is nSpace x nTime
    title : string, optional
        Title of the figure. Default is None.
    cmap : string, optional
        Color type for colormap. Default is 'inferno'.
    fig : matplotlib.figure.Figure, optional
        Existing figure to plot on. If None, a new figure is created.
    ax : matplotlib.axes.Axes, optional
        Existing axes to plot on. If None, new axes are created.
    **kwargs : dict, optional
        Additional keyword arguments passed to the plotting function.

    Return
    --------------
    fig, ax : Matplotlib figure & axes objects,
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

def temp_kanger(t, t_shift = 0):
    '''
    For an array of times in days, return timeseries of temperature for Kangerlussuaq, Greenland. Any shift of temperature (e.g., due to global warming) can be added using t_shift.
    
    '''
    # Kangerlussuaq average temperature:
    t_kanger = np.array([-19.7, -21.0, -17., -8.4, 2.3, 8.4,
    10.7, 8.5, 3.1, -6.0, -12.0, -16.9])
    t_amp = (t_kanger - t_kanger.mean()).max()
    return t_amp*np.sin(np.pi/180 * t - np.pi/2) + t_kanger.mean() + t_shift
