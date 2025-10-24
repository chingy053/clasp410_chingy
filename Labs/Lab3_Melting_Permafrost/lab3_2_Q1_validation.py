#!/usr/bin/python3
'''
This file solve Question 1 (prompt as shown below) from Lab 3 and produce the plots.

Question 1: Build a function that solves the heat equation given a set of initial conditions, boundary
conditions, end points for the spatial and time domains, and the time and space step sizes. It should return three arrays: a vector of grid points, a vector of time points, and a two-dimensional array of temperatures. Make your function check to see if your selected configuration is numerically stable; it should stop gracefully if not. Use this function to solve the example problem described above. Validate your results against the solution.

Set: 
    0 <= x <= 1 m
    0 <= t <= 0.2 s
    c2 = 1 m^2/s
    dx = 0.2 m
    dt = 0.02 s
    Boundary condition:
        U(0, t) = U(1, t) = 0
        U(x, 0) = 4x - 4x**2 

Verify:
    By comparing the solution with Table 1. 
        
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab3_1_functions import solve_heat, plot_heatsolve, temp_kanger
#---------------------------------------------------------------
t_1,x_1,U_1 = solve_heat(xstop=1, tstop = 0.2, dx=0.2, dt = 0.02, c2 = 1, lowerbound=0, set_ic = 'validation')
print(U_1)