#!/usr/bin/python3
'''
This code is based on Feuillebois et al. (1995) Equations 14-23, solving for the freeze of liquid droplet using heat diffusion equations.
'''

import numpy as np
import matplotlib.pyplot as plt 

def solve_freeze(tstop=5.0, xstop=1.0, dt=1.125e-05, dx=0.005, epsilon=0.01, R=1e-5, rho_s=920.0, c_s=2100.0, k_s=2.2):
    """
    Solve the 1-D Stefan freezing problem for a spherical droplet using an
    explicit forward-difference scheme.

    Parameters
    ----------
    tstop : float
        Nondimensional time. Default to 5.0.
    xstop : float
        Nondimensional spatial domain. Default to 1.0 (starting from the outer shell).
    dt : float
        Time step size. Default to 1.125e-05.
    dx : float
        Spatial step size, Default to 0.005.
    epsilon : float
        Dimensionless parameter. Default to 0.01.
    R : float
        Physical radius of droplet (m). Default to 10 micron.
    rho_s : float
        Density of solid phase (kg/m^3). Default to 920.0 for ice.
    c_s : float
        Specific heat of solid (J/kg/K). Default to 2100.0 for ice.
    k_s : float
        Thermal conductivity of solid (W/m/K). Default to 2.2.

    Returns
    -------
    t : 1-D array
        Nondimensional time array from 0 to tstop.
    x : 1-D array
        Nondimensional spatial grid from xstop down to 0.
    U : 2-D array
        Nondimensional temperature field U(x, t). U = 1 at the outer
        boundary and U = 0 in the liquid region and at the
        freezing front.
    s : 1-D array
        Nondimensional freezing-front position.
    r_i : 1-D array
        Physical freezing front radius.
    du_dx : 1-D array
        Spatial derivative of U at the interface.
    ds_dt : 1-D array
        Rate of freezing front motion in nondimensional time.
    t_phys : 1-D array
        Physical time (s).
    x_phys : 1-D array
        Physical radius coordinate (m).
    t_char : 1-D array
        Thermal diffusion timescale (s).
    """

    # Get grid sizes (plus one to include "0" as well)
    N = int(tstop/dt)+1
    M = int(xstop/dx)+1

    # Set up space and time grid
    t = np.linspace(0, tstop, N)
    x = np.linspace(xstop, 0, M) # x go from 1 to 0 instead

    # Set s
    s = np.zeros(N)
    s[0] = 1.0

    # Create solution matrix; set initial condition
    U = np.zeros([M, N])
    # Initial condition:
    U[:, 0] = 0.0 # when t = 0, s(0) = 1, U(s(t),t) = 0, so U(1,0) = 0. Freezing start point.
    U[x >= s[0], 0] = 1.0 # when x = 1, U = 1

    # Get r_def
    r_def = epsilon*(dt/dx**2)

    # Set du_dx, ds_dt
    du_dx = np.zeros(N)
    ds_dt = np.zeros(N)

    # Radius of the liquid droplet
    # R is given as function argument

    # Freezing front radius r_i
    # s = r_i / R
    r_i = np.zeros(N)
    r_i[0] = R

    # Solve our equation
    for j in range(N-1):

        # Make a copy of U so the new variable is a 1-D array
        # This way the values don't overwrite
        un   = U[:, j].copy()
        unew = un.copy()

        # Always enforece outer boundary at x = 1, U = 1
        unew[0] = 1.0

        # Find freezing point index
        i_s = np.searchsorted(-x, -s[j])   
        if i_s == 0:
            i_s = 1

        # Assume liquid region (x < s) T=Tf, u=0
        unew[i_s:] = 0.0

        # Equation [19]: Classic heat diffusion equation
        # Only apply to the frozen part for each time step
        for i in range(1, i_s):
            unew[i] = ((1 - 2.0 * r_def) * un[i] +
                       r_def * (un[i+1] + un[i-1]))

        # Equation [21]: boundary condition u(s(t),t) = 0
        # Freezing front u(s,t)=0 at x[i_s]
        unew[i_s] = 0.0

        # Save new temperature profile to U
        U[:, j+1] = unew

        # Equation [22]: du/dx|{x=s} = -s(t) * (ds(t)/dt)
        # This is Stefan condition
        # Using backward difference for spatial derivative
        du_dx[j] = (unew[i_s] - unew[i_s-1]) / (x[i_s] - x[i_s-1])

        if s[j] > 0:
            ds_dt[j] = -du_dx[j] / s[j]
        else:
            ds_dt[j] = 0.0

        s[j+1] = s[j] + ds_dt[j] * dt

        # Optional: stop if interface essentially reaches the center
        if s[j+1] <= dx:
            s[j+1] = dx

        # Save the freezing front radius as r_i = s * R
        r_i[j+1] = s[j+1] * R

    # ---------------------------------------------------------
    # Add dimensional quantities
    # ---------------------------------------------------------

    # Characteristic thermal diffusion time (from nondimensionalization)
    t_char = (R**2) * rho_s * c_s / k_s

    # Physical time array
    t_phys = t * t_char / epsilon

    # Physical spatial grid
    x_phys = x * R

    return (t, x, U, s, r_i, du_dx, ds_dt,
            t_phys, x_phys, t_char)

[t_1,x_1,U_1,s_1,r_i_1,du_dx_1, ds_dt_1,t_phys_1, x_phys_1, t_char_1]=solve_freeze()