#!/usr/bin/env python3

'''
This file solve Question 1 (prompt as shown below) using a wider than it is tall grid from Lab 4 to verify the functions.

Question 1: 
Build the model as described in the next section. Discuss your implementation in the Methodology section of your report. Test your code using a 3x3 grid, 100% chance of spread, zero initial bare spots, and only the center cell on fire. Demonstrate correct behavior from iteration 0 to 1 and iteration 1 to 2. Repeat this test with a larger grid that is wider than it is tall. Show the results of this test in your Methodology section.
'''
#---------------------------------------------------------------
import os
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation, PillowWriter
from lab4_1_functions import forest_fire, plot_forest2d, plot_forest2d_animation
#---------------------------------------------------------------
# Setups:
# 1) Grid: 5x7
# 2) Pspread: 100%
# 3) Pignite: N/A (fire starts from the center cell)
# 4) Pbare: 0%
# 5) Pfetal: N/A
# 6) Timesteps: 7
#---------------------------------------------------------------

plot_forest2d(isize=5,jsize=7,nstep=7,save_dir='./', txt_label = True,save_name='lab4_3_Q1_veri_5x7_fire_at_center')
plot_forest2d_animation(isize=5,jsize=7,nstep=7, txt_label = True, 
              save_dir='./', 
              save_name='lab4_3_Q1_veri_5x7_fire_at_center')