#!/usr/bin/python3

'''
This file solve Question 1 (prompt as shown below) from Lab 2 and produce the plots.

Question 1: How does the performance of the Euler method solver compare to
the 8th-order DOP853 method for both sets of equations?

Set: 
    a = 1, b = 2, c = 1, and d = 3
    N1 = 0.3 and N2 = 0.6
    Integrate for 100 years
        For the competition model, dt = 1yr
        For the predator-prey model, dt = 0.05yr

Verify:
    By repoducing the example in Figure 1. Play with the time step size and compare the two ODE solvers.You may describe your results in qualitative terms, but show examples to support your claims
        
Plot : time versus population to see how N1 and N2 change over time.
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab2_1_functions import dNdt_pypdt, dNdt_comp, euler_solve, solve_rk8

#---------------------------------------------------------------

# -------------------------------------------------------------------------------- 
#                                       Verify
# -------------------------------------------------------------------------------- 
# ------------> Prey-Predator
[time_E_PP_Q1,N1_E_PP_Q1,N2_E_PP_Q1] = euler_solve(dNdt_pypdt,N1_init=0.3, N2_init=0.6, dt=0.05, t_final=101.0)
[time_R_PP_Q1,N1_R_PP_Q1,N2_R_PP_Q1] = solve_rk8(dNdt_pypdt,N1_init=0.3, N2_init=0.6, dt=0.05, t_final=101.0)
# ------------> Competing
[time_E_C_Q1,N1_E_C_Q1,N2_E_C_Q1] = euler_solve(dNdt_comp,N1_init=0.3, N2_init=0.6, dt=1.0, t_final=101.0)
[time_R_C_Q1,N1_R_C_Q1,N2_R_C_Q1] = solve_rk8(dNdt_comp,N1_init=0.3, N2_init=0.6, dt=1.0, t_final=101.0)
# ------------> Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.plot(time_E_C_Q1,N1_E_C_Q1,"r", linewidth=2, label="N1, Euler")
ax1.plot(time_E_C_Q1,N2_E_C_Q1,"b", linewidth=2, label="N2, Euler")
ax1.plot(time_R_C_Q1,N1_R_C_Q1,"r:", linewidth=2, label="N1, RK8")
ax1.plot(time_R_C_Q1,N2_R_C_Q1,"b:", linewidth=2, label="N2, RK8")
ax1.set_xlabel('Time (years)')
ax1.set_ylabel('Population')
ax1.legend()
ax1.set_title('Lotka-Voterra Competition Model')
ax1.grid(True)

ax2.plot(time_E_PP_Q1,N1_E_PP_Q1,"r", linewidth=2, label="N1 (Prey), Euler")
ax2.plot(time_E_PP_Q1,N2_E_PP_Q1,"b", linewidth=2, label="N2 (Predator), Euler")
ax2.plot(time_R_PP_Q1,N1_R_PP_Q1,"r:", linewidth=2, label="N1 (Prey), RK8")
ax2.plot(time_R_PP_Q1,N2_R_PP_Q1,"b:", linewidth=2, label="N2 (Predator), RK8")
ax2.set_xlabel('Time (years)')
ax2.set_ylabel('Population/Carrying Cap.')
ax2.legend()
ax2.set_title('Lotka-Voterra Predator-Prey Model')
ax2.grid(True)

plt.rcParams.update({'font.size': 16})
plt.savefig("plot_lab2_2_Q1_f1_verify.png")
plt.close()

# -------------------------------------------------------------------------------- 
#                                Varying Time Steps
# --------------------------------------------------------------------------------
# ------------> Set up the variables
time_steps_PP = np.arange(0.01,0.21,0.02)
time_steps_C = np.arange(0.5,5.5,0.5)

# -------------------------------- Prey-Predator ---------------------------------
fig3, axs = plt.subplots(2, 2, figsize=(19, 11))
ax3, ax4, ax5, ax6 = axs.ravel() 
#fig3.canvas.manager.full_screen_toggle() # Maxiumize the figure

for g in range(len(time_steps_PP)):
    # ------------> Calculation population
    [time_E_PP_Q1_f,N1_E_PP_Q1_f,N2_E_PP_Q1_f] = euler_solve(dNdt_pypdt,N1_init=0.3, N2_init=0.6, dt=time_steps_PP[g], t_final=101.0)
    [time_R_PP_Q1_f,N1_R_PP_Q1_f,N2_R_PP_Q1_f] = solve_rk8(dNdt_pypdt,N1_init=0.3, N2_init=0.6, dt=time_steps_PP[g], t_final=101.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(time_steps_PP)))
    # ------------> Plot

    # ---> N1 (Euler)
    ax3.plot(time_E_PP_Q1_f, N1_E_PP_Q1_f, color = def_colors[g], linewidth=2, label = f'dt = {time_steps_PP[g]:.2f}')
    ax3.set_ylim(-1,2)
    ax3.set_xlim(0, 150)
    ax3.set_ylabel('Population/Carrying Cap.')
    ax3.legend(loc='best')
    ax3.set_title('Predator-Prey Model using Euler: N1 (Prey)')
    ax3.grid(True)

    # ---> N2 (Euler)
    ax4.plot(time_E_PP_Q1_f, N2_E_PP_Q1_f, color = def_colors[g], linewidth=2, label = f'dt = {time_steps_PP[g]:.2f}')
    ax4.set_ylim(-1,2)
    ax4.set_xlim(0, 150)
    ax4.set_ylabel('Population/Carrying Cap.')
    ax4.legend(loc='best')
    ax4.set_title('Predator-Prey Model using Euler: N2 (Predator)')
    ax4.grid(True)

    # ---> N1 (RK8)
    ax5.plot(time_R_PP_Q1_f, N1_R_PP_Q1_f, color = def_colors[g], linewidth=2, label = f'dt = {time_steps_PP[g]:.2f}')
    # ax5.set_ylim(-1,2)
    ax5.set_xlim(0, 150)
    ax5.set_xlabel('Time (years)')
    ax5.set_ylabel('Population/Carrying Cap.')
    ax5.legend(loc='best')
    ax5.set_title('Predator-Prey Model using RK8: N1 (Prey)')
    ax5.grid(True)

    # ---> N2 (RK8)
    ax6.plot(time_R_PP_Q1_f, N2_R_PP_Q1_f, color = def_colors[g], linewidth=2, label = f'dt = {time_steps_PP[g]:.2f}')
    # ax5.set_ylim(-1,2)
    ax6.set_xlim(0, 150)
    ax6.set_xlabel('Time (years)')
    ax6.set_ylabel('Population/Carrying Cap.')
    ax6.legend(loc='best')
    ax6.set_title('Predator-Prey Model using RK8: N2 (Predator)')
    ax6.grid(True)

fig3.suptitle("How do time steps affect the performance of the Euler method and the 8th-order DOP853 method?", fontsize=24)
fig3.text(0.5, 0.94, "Coefficients: a = 1, b = 2, c = 1, d = 3", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig3.savefig("plot_lab2_2_Q1_f2_Prey_Predator_change_dt.png")
plt.close()
# --------------------------------- Competing ---------------------------------
fig4, axs2 = plt.subplots(2, 2, figsize=(19, 11))
ax7, ax8, ax9, ax10 = axs2.ravel() 
for k in range(len(time_steps_C)):
    # ------------> Calculation population
    [time_E_C_Q1_f,N1_E_C_Q1_f,N2_E_C_Q1_f] = euler_solve(dNdt_comp,N1_init=0.3, N2_init=0.6, dt=time_steps_C[k], t_final=101.0)
    [time_R_C_Q1_f,N1_R_C_Q1_f,N2_R_C_Q1_f] = solve_rk8(dNdt_comp,N1_init=0.3, N2_init=0.6, dt=time_steps_C[k], t_final=101.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(time_steps_C)))
    # ------------> Plot

    # ---> N1 (Euler)
    ax7.plot(time_E_C_Q1_f, N1_E_C_Q1_f, color = def_colors[k], linewidth=2, label = f'dt = {time_steps_C[k]:.2f}')
    ax7.set_ylim(-0.5,1.3)
    ax7.set_xlim(0, 150)
    ax7.set_ylabel('Population/Carrying Cap.')
    ax7.legend(loc='best')
    ax7.set_title('Competition Model using Euler: N1 ')
    ax7.grid(True)

    # ---> N2 (Euler)
    ax8.plot(time_E_C_Q1_f, N2_E_C_Q1_f, color = def_colors[k], linewidth=2, label = f'dt = {time_steps_C[k]:.2f}')
    ax8.set_ylim(-0.5,1.3)
    ax8.set_xlim(0, 150)
    ax8.set_ylabel('Population/Carrying Cap.')
    ax8.legend(loc='best')
    ax8.set_title('Competition Model using Euler: N2 ')
    ax8.grid(True)

    # ---> N1 (RK8)
    ax9.plot(time_R_C_Q1_f, N1_R_C_Q1_f, color = def_colors[k], linewidth=2, label = f'dt = {time_steps_C[k]:.2f}')
    # ax9.set_ylim(-1,2)
    ax9.set_xlim(0, 150)
    ax9.set_xlabel('Time (years)')
    ax9.set_ylabel('Population/Carrying Cap.')
    ax9.legend(loc='best')
    ax9.set_title('Competition Model using RK8: N1 ')
    ax9.grid(True)

    # ---> N2 (RK8)
    ax10.plot(time_R_C_Q1_f, N2_R_C_Q1_f, color = def_colors[k], linewidth=2, label = f'dt = {time_steps_C[k]:.2f}')
    # ax9.set_ylim(-1,2)
    ax10.set_xlim(0, 150)
    ax10.set_xlabel('Time (years)')
    ax10.set_ylabel('Population/Carrying Cap.')
    ax10.legend(loc='best')
    ax10.set_title('Competition Model using RK8: N2 ')
    ax10.grid(True)

fig4.suptitle("How do time steps affect the performance of the Euler method and the 8th-order DOP853 method?", fontsize=24)
fig4.text(0.5, 0.94, "Coefficients: a = 1, b = 2, c = 1, d = 3", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig4.savefig("plot_lab2_2_Q1_f3_Competition_change_dt.png")
plt.close()