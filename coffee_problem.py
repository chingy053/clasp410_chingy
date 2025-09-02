#!/usr/bin/python3
'''
Solve the voffee problem to learn how to drink coffee effectively
Tell Sara how to run your code
'''

import numpy as np
import matplotlib.pyplot as plt ; plt.ion()

def solve_temp(t,T_init, T_env, k):
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

Tnow = solve_temp(10.0,90.,20.,1/300.)
print('Tnow = ',Tnow)
t = np.arange(0,600,0.5)
Temp = solve_temp(t,90,20,1/300.)
plt.plot(t,Temp)
plt.show()


