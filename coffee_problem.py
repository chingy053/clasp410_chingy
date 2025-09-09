#!/usr/bin/python3
'''
Solve the coffee problem to learn how to drink coffee effectively
Tell Sara how to run your code
'''

import numpy as np
import matplotlib.pyplot as plt ; plt.ion()

def solve_temp(t, T_init = 90., T_env = 20.0, k = 1/300.):
    '''
    This function returns temperature as a function of time 
    using Newton's law of cooling

    Parameters
    -----------
    t: Numpy array
        An array of time values in seconds
    T_init: floating point, defaults to 90.
        Initial tempreature in Celsius.
    T_env: floating point, defaults to 20.
        Ambient air temparture in Celsisu
    k: floating point, defaults to 1/300.
        Heat transfer coefficient in 1/s.

    Returns
    ---------
    T_coffee: Numpy array
        Temperature corresponding to time t

    '''
    T_coffee = T_env + (T_init - T_env) * np.exp(-k*t)

    return T_coffee

def time_to_temp(T_final, T_init = 90., T_env = 20.0, k = 1/300.):
    '''
    Given a target temperature, determine how long it takes to reach the target temp using Newton's law of cooling

    Parameters
    -----------
    T_final: floating point
        Final tempearture in C.
    T_init: floating point, defaults to 90.
        Initial tempreature in Celsius.
    T_env: floating point, defaults to 20.
        Ambient air temparture in Celsisu
    k: floating point, defaults to 1/300.
        Heat transfer coefficient in 1/s.

    Returns
    ---------
    t : float
        time, in seconds, to cool to target T_final

    '''

    t = (-1/k) * np.log((T_final - T_env) / (T_init - T_env))
    return t

def verify_code():
    '''
    Verify that our implementation is correct
    '''
    t_real = 60. * 10.76
    k = np.log(95./110.) / -120.
    t_code = time_to_temp(120.,T_init = 180., T_env = 70., k = k)

    print("Target solution is :", t_real)
    print("Numerical solution is ", t_code)
    print("Difference is ",t_real - t_code)


    
# Solve for the actual problem using the functions declared above.
t_1 = time_to_temp(65)              # Add cream at T=65 to get to 60
t_2 = time_to_temp(60,T_init=85)    # Add cream immediately
t_c = time_to_temp(60)              # Control case: No cream

print("TIME TO DRINKABLE COFFEE:")
print(f"Control case = {t_c:.2f}s")
print(f"Add cream later = {t_1:.1f}s")
print(f"Add cream now = {t_2:.1f}s")

# Create time series of temperatures for cooling coffee
t = np.arange(0,600,0.5)
Temp1 = solve_temp(t) # also the same as control case
Temp2 = solve_temp(t, T_init=85.)

#Create our figure and plot stuff!
fig, ax = plt.subplots(1,1,figsize=(10, 5))
plt.style.use('fivethirtyeight')
ax.plot(t,Temp1, label=f'Add Cream Later (T={t_1:.1f}s)')
ax.axvline(x=171, linestyle='--', linewidth=1)
ax.plot(t,Temp2, label=f'Add Cream Now (T={t_2:.1f}s)')
ax.legend()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')
ax.set_title('When to add cream: Getting coffee cooled quickly')
