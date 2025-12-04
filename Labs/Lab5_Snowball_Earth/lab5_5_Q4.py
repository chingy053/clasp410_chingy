#!/usr/bin/env python3

'''
This file solve Question 4 (prompt as shown below) from Lab 5 Snowball Earth.

Question 4: 
xplore the impact of solar forcing on your snowball Earth. Create a ”solar multiplier” factor, γ, which is applied to your insolation term in your solver, i.e., insol = gamma * insolation(S0, lats).
Starting with the ”cold Earth” initial condition, run your simulation with γ = 0.4. Use the result as an initial conditition for another simulation, increasing γ by 0.05. Repeat this until γ = 1.4. At this point, ”turn around”: lower γ by 0.05, run another simulation, repeat until γ = 0.4 again. Each time, use the previous result as the initial condition to the next simulation. Plot average global temperature versus γ. Answer the science question, does the snowball Earth hypothesis represent an equilibrium solution that is stable? What does this plot tell you about the stability of the different equilibria? Given the large range for γ and considering the historical variation of S0, do you think that snowball Earth is a valid hypothesis?

'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from lab5_1_functions import gen_grid, temp_warm, insolation, snowball_earth, test_functions

plt.style.use('fivethirtyeight')
#---------------------------------------------------------------
# Create an array of gamma
gamma_start = 0.4
gamma_end = 1.4
gamma_step = 0.05

gammas_1   = np.arange(gamma_start, gamma_end+gamma_step, gamma_step)
gammas_2 = np.arange(gamma_end-gamma_step, gamma_start-gamma_step, -gamma_step)
gammas_range = np.concatenate([gammas_1, gammas_2])

# Starting with a cold Earth
lats, Temp_41 = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,solar=1370.,gamma=1,init_cond=-60)

# Apply different gamma
Temp_save = np.zeros((len(Temp_41), len(gammas_range)))
Temp_global_mean = np.zeros(len(gammas_range))
for ii in range(len(gammas_range)):
    if ii == 0:
        Temp_updated = Temp_41
    else:
        Temp_updated = Temp_save[:,ii-1]
    lats, Temp_new = snowball_earth(apply_spherecorr=True,apply_insol=True,lam=80.0,emiss = 0.7,solar=1370.,gamma=gammas_range[ii],init_cond=Temp_updated)
    print(gammas_range[ii])
    Temp_save[:,ii] = Temp_new
    Temp_global_mean[ii] = np.mean(Temp_new)
    print(gammas_range[ii],Temp_global_mean[ii])

fig1, ax1 = plt.subplots(1,1,figsize=(16, 10))
ax1.plot(gammas_range[:21],Temp_global_mean[:21], "k.",linewidth=3,markersize=30,label="Increasing γ from 0.4 to 1.4")
ax1.plot(gammas_range[21:],Temp_global_mean[21:], "r.",linewidth=3,markersize=30,label="Decreasing γ from 1.4 to 0.4")
ax1.legend(loc="lower right")
ax1.set_ylabel(r'Global Mean Temperature ($^{\circ}C$)')
ax1.set_xlabel('Solar Multiplier Factor (γ)')
ax1.set_title('Impact of Solar Forcing on Global Mean Temperature')
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.text(0.4, 13, 
        "diffusivity = 80 m²/s\n"
        "emissivity = 0.7\n"
        "constant albedo = 0.3 or 0.6\n"
        "dynamic albedo (water) = 0.3\n"
        "dynamic albedo (ice) = 0.6\n",
         fontsize=16, color='black')
plt.savefig("plot_lab5_5_Q4.png")
plt.close()



