#!/usr/bin/python3
'''
Use Lotka-Voterra competition and predator-prey ODE equation sets to predict the populations of two biological species. Also use two methods, one with first-order-accurate Euler and another with Dormand-Prince embedded 8th-order Runge-Kutta.

This file contains all the defined functions. These functions will be used in other python scipts of Lab 2.
'''

import numpy as np
import matplotlib.pyplot as plt ; plt.ion()

def dNdt_pypdt(t, N, a=1, b=2, c=1, d=3):
    '''
    This function calculates the Lotka-Volterra prey-pradator equations for two species. Given normalized populations, `N1` and `N2`, as well as the four coefficients representing population growth and decline, calculate the time derivatives dN_1/dt and dN_2/dt and return to the caller. This function accepts `t`, or time, as an input parameter to be compliant with Scipy's ODE solver. However, it is not used in this function.

    Parameters
    ----------
    t : float
        The current time (not used here).
    N : two-element list
        The current value of N1 and N2 as a list (e.g., [N1, N2]).
    a, b, c, d : float, defaults = 1, 2, 1, 3
        The value of the Lotka-Volterra coefficients.

    Returns
    -------
    dN1dt, dN2dt : floats
        The time derivatives of `N1` and `N2`.
    '''

    # Here, N is a two-element list such that N1=N[0] and N2=N[1]
    dN1dt = a*N[0] - b*N[0]*N[1]
    dN2dt = -c*N[1] + d*N[1]*N[0]
    return dN1dt, dN2dt

def dNdt_comp(t, N, a=1, b=2, c=1, d=3):
    '''
    This function calculates the Lotka-Volterra competition equations for two species. Given normalized populations, `N1` and `N2`, as well as the four coefficients representing population growth and decline, calculate the time derivatives dN_1/dt and dN_2/dt and return to the caller. This function accepts `t`, or time, as an input parameter to be compliant with Scipy's ODE solver. However, it is not used in this function.

    Parameters
    ----------
    t : float
        The current time (not used here).
    N : two-element list
        The current value of N1 and N2 as a list (e.g., [N1, N2]).
    a, b, c, d : float, defaults = 1, 2, 1, 3
        The value of the Lotka-Volterra coefficients.

    Returns
    -------
    dN1dt, dN2dt : floats
        The time derivatives of `N1` and `N2`.
    '''

    # Here, N is a two-element list such that N1=N[0] and N2=N[1]
    dN1dt = a*N[0]*(1-N[0]) - b*N[0]*N[1]
    dN2dt = c*N[1]*(1-N[1]) - d*N[1]*N[0]
    return dN1dt, dN2dt

def euler_solve(func, N1_init=.5, N2_init=.5, dt=.1, t_final=100.0, **kwargs):
    '''
    Solve an ordinary differential equation using Euler's method (first oder) where 
        f(t+dt) = f(t0) + dt*f'(t+dt) + (1/2)*dt^2*f''(t+dt) + ...
    for Lotka-Volterra competition and prey-predator equations.
    Extra kwargs are passed to the functions
    
    Parameters
    ----------
    func : function
        A python function that takes `time`, [`N1`, `N2`] as inputs and
        returns the time derivative of N1 and N2.
    N1_init : float, default = 0.5
        Initial normalized population of a species, ranging from (0,1].
    N2_init : float, default = 0.5
        Initial normalized population of a second species, ranging from (0,1].
    dt : float, default = 0.1
        Increment of time
    t_final : float, default = 100.0
        The final time of the time range.
    **kwargs : any other extra keyword arguments
        Any other keyword arugments that may not be used in this function but in the input function.

    Returns
    ----------
    time : Numpy array
        The time array
    N1 : Numpy array
        The population of N1 species over time.
    N2 : Numpy array
        The population of N2 species over time.
    '''

    # Configure our problem:
    time = np.arange(0,t_final,dt)
    N1 = np.zeros(time.size)
    N2 = np.zeros(time.size)
    N1[0] = N1_init
    N2[0] = N2_init

    # Important code goes here #
    for i in range(1, time.size):
        dN1, dN2 = func(time[i], [N1[i-1], N2[i-1]],**kwargs)
        N1[i] = N1[i-1] + dt * dN1
        N2[i] = N2[i-1] + dt * dN2

    return time, N1, N2

def solve_rk8(func, N1_init=.5, N2_init=.5, dt=10, t_final=100.0,
a=1, b=2, c=1, d=3):
    '''
    Solve the Lotka-Volterra competition and prey-predator equations using
    Scipy's ODE class and the adaptive step 8th order solver.

    Parameters
    ----------
    func : function
        A python function that takes `time`, [`N1`, `N2`] as inputs and
        returns the time derivative of N1 and N2.
    N1_init, N2_init : float
        Initial conditions for `N1` and `N2`, ranging from (0,1].
    dTt : float, default = 10
        Largest timestep allowed in years.
    t_final : float, default = 100
        Integrate until this value is reached, in years.
    a, b, c, d : float, default = 1, 2, 1, 3
        Lotka-Volterra coefficient values

    Returns
    ----------
    time : Numpy array
        Time elapsed in years.
    N1, N2 : Numpy arrays
        Normalized population density solutions.
    '''
    from scipy.integrate import solve_ivp

    # Configure the initial value problem solver
    result = solve_ivp(func, [0, t_final], [N1_init, N2_init],
    args=[a, b, c, d], method='DOP853', max_step=dt)

    # Perform the integration
    time, N1, N2 = result.t, result.y[0, :], result.y[1, :]

    # Return values to caller
    return time, N1, N2

# for i in range(10):
#     plt.plot(np.arange(5) + i)
#     plt.text(5,3.5+i,f"line#{i}")