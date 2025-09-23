#!/usr/bin/python3
'''
This file complies the basic functions needed for solving the N-layer atmosphere energy balance problem for Lab 01 and all subparts.

To reproduce the values and plots in my report, run the scripts in the following order: 
1. lab1_1_nlayer.py
2. lab1_2_Q3.py
'''

import numpy as np
import matplotlib.pyplot as plt

#---------> Physical Constants
sigma = 5.67e-8 #Units: W/m2/K4

#---------> Define all the functions
def n_layer_atmos(nlayers, epsilon=1,albedo=0.33,s0=1350, debug = False):
    '''
    Solve the n-layer atomsphere energy balance problem in terms of fluxes rather than temperatures. This function returns the flux in W/m^2 at each layer.

    Parameters
    ----------------
    nlayers: int
        The number of layers.
    epsilon: float
        The emissivity of each layer, ranging between 0 and 1. Assumed to be the same in all atmospheric layer in this problem. The default value is 1, meaning the layer acts like a black body - 100% absorbing and emitting all the radiation with no transmission.
    albedo: float
        The albedo or reflectivity of the planetary surface, ranging between 0 and 1. The default value is set to be 0.33, approximately the real albedo of the Earth.
    s0: float
        Incoming solar radiation flux in W/m^2. The default value is 1350 W/m^2.
    debug: bool
        When it is set to be true, it will print out elements in matrix A.
    A: float matrix
        Coefficient matrix for the n-layer energy balance model. The number of rows represents the surface and atmospheric layers. Each column represents a flux term from each layer. The full set of energy balance equation is A*F=b. Negative value means outgoing; positive value is incoming.
    b: float vector
        The right side of the equation, representing forcing. 
    Ainv: float matrix
        The inverse matrix of A.

    Return
    ----------------
    fluxes: float vector
        The calculated radiation fluxes of Earth surface and each atmospheric layer.
    '''
    #---------> Create array of coefficients, an N+1xN+1 array:
    A = np.zeros([nlayers+1, nlayers+1])
    b = np.zeros(nlayers+1)
    #---------> Populate based on our model:
    for i in range(nlayers+1):
        for j in range(nlayers+1):
            if i == 0 and j != 0:
                A[i,j] = (1-epsilon)**(j-1)
            elif i == j:
                A[i, j] = -2
            else:
                expon = np.abs(i-j)-1
                A[i, j] = epsilon*(1-epsilon)**expon
    A[0,0] = -1
    b[0] = -(1./4.)*s0*(1-albedo)

    #---------> Invert matrix:
    Ainv = np.linalg.inv(A)

    #---------> Get solution:
    fluxes = np.matmul(Ainv, b) # Note our use of matrix    multiplication!

    #---------> Debug
    if debug == True:
        nn = 1
        ee = 0.255
        print(n_layer_atmos(nn,epsilon=ee))
        print(Stefan_Boltzmann(n_layer_atmos(nn,epsilon=ee),ee))

    return fluxes

#---------> Convert fluxes to temperature!
def Stefan_Boltzmann(flux, epsilon=1):
    '''
    Convert fluxes (W/m^2) to temperature (K) using Stefan Boltzmann's Law.

    Parameters
    ----------------
    flux: float vector
        Fluxes of the surface and each layer in W/m^2.
    epsilon: float
        The emissivity of each layer, ranging between 0 and 1. Assumed to be the same in all atmospheric layer in this problem. The default value is 1, meaning the layer acts like a black body - 100% absorbing and emitting all the radiation with no transmission.

        
    Return
    ----------------
    Temp: float vector
        The calculated temperatures of Earth surface and each atmospheric layer.
    '''
    Temp = (flux/sigma/epsilon)**(1./4.)
    #---------> Assume Earth is a blackbody
    Temp[0] = (flux[0]/sigma/1)**(1./4.)
    return Temp

#---------> N-layer Atmosphere Problem for Nuclear Winter
def n_layer_nuclear_winter(nlayers, epsilon=1,albedo_toa=0,s0=1350, debug = False):
    '''
    Solve the n-layer atomsphere energy balance problem in terms of fluxes for nuclear winter case, which the top of atmosphere absorbs all incoming solar radiation. This function returns the flux in W/m^2 at each layer.

    Parameters
    ----------------
    nlayers: int
        The number of layers.
    epsilon: float
        The emissivity of each layer, ranging between 0 and 1. Assumed to be the same in all atmospheric layer in this problem. The default value is 1, meaning the layer acts like a black body - 100% absorbing and emitting all the radiation with no transmission.
    albedo: float
        The albedo or reflectivity of the planetary surface, ranging between 0 and 1. The default value is set to be 0.33, approximately the real albedo of the Earth.
    s0: float
        Incoming solar radiation flux in W/m^2. The default value is 1350 W/m^2.
    debug: bool
        When it is set to be true, it will print out elements in matrix A.
    A: float matrix
        Coefficient matrix for the n-layer energy balance model. The number of rows represents the surface and atmospheric layers. Each column represents a flux term from each layer. The full set of energy balance equation is A*F=b. Negative value means outgoing; positive value is incoming.
    b: float vector
        The right side of the equation, representing forcing. 
    Ainv: float matrix
        The inverse matrix of A.

    Return
    ----------------
    fluxes: float vector
        The calculated radiation fluxes of Earth surface and each atmospheric layer.
    '''
    #---------> Create array of coefficients, an N+1xN+1 array:
    A = np.zeros([nlayers+1, nlayers+1])
    b = np.zeros(nlayers+1)
    #---------> Populate based on our model:
    for i in range(nlayers+1):
        for j in range(nlayers+1):
            if i == 0 and j != 0:
                A[i,j] = (1-epsilon)**(j-1)
            elif i == j:
                A[i, j] = -2
            else:
                expon = np.abs(i-j)-1
                A[i, j] = epsilon*(1-epsilon)**expon
    A[0,0] = -1
    b[-1] = -(1./4.)*s0*(1-albedo_toa) # the top layer absorbs all the solar radiation

    #---------> Invert matrix:
    Ainv = np.linalg.inv(A)

    #---------> Get solution:
    fluxes = np.matmul(Ainv, b) # Note our use of matrix    multiplication!

    #---------> Debug
    if debug == True:
        nn = 5
        ee = 0.5
        print(b)
        print(n_layer_atmos(nn,epsilon=ee))
        print(Stefan_Boltzmann(n_layer_nuclear_winter(nn,epsilon=ee),ee))

    return fluxes