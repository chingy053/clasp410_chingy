#!/usr/bin/python3
'''
This file solve Question 2 (prompt as shown below) from Lab 2 and produce the plots.

Question 2: Focus on the competition model equations. Vary initial conditions and the different coefficients. Try to create conditions that result in an equilibrium rather than one or both species becoming extinct. Answer the question, How do the initial conditions and coefficient values affect the final result and general behavior of the two species? Describe in qualitative terms, but provide examples.

Plot : time versus population to see how N1 and N2 change over time.
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab2_1_functions import dNdt_pypdt, dNdt_comp, euler_solve, solve_rk8

#---------------------------------------------------------------
# 2-1: Varying initial conditions
#---------------------------------------------------------------

# ------------> Set up the variables
init_cond = np.arange(0.1,1.0,0.1)

fig1, axs1 = plt.subplots(2, 2, figsize=(19, 11))
ax1, ax2, ax3, ax4 = axs1.ravel() 

for i in range(len(init_cond)):
    # ------------> Varying N1 initial condition
    [time_E_Q2_N1,N1_E_Q2_N1,N2_E_Q2_N1] = euler_solve(dNdt_comp, N1_init=init_cond[i], dt=1.0, t_final=21.0)
    [time_R_Q2_N1,N1_R_Q2_N1,N2_R_Q2_N1] = solve_rk8(dNdt_comp,N1_init=init_cond[i], dt=1.0, t_final=21.0)

    # ------------> Varying N2 initial condition
    [time_E_Q2_N2,N1_E_Q2_N2,N2_E_Q2_N2] = euler_solve(dNdt_comp, N2_init=init_cond[i], dt=1.0, t_final=21.0)
    [time_R_Q2_N2,N1_R_Q2_N2,N2_R_Q2_N2] = solve_rk8(dNdt_comp,N2_init=init_cond[i], dt=1.0, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(init_cond)))
    # ------------> Plot

    # ---> Euler: Varying N1
    ax1.plot(time_E_Q2_N1, N1_E_Q2_N1, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax1.set_ylim(-0.25,1.5)
    ax1.set_xlim(0, 25)
    ax1.set_ylabel('Population/Carrying Cap.')
    # ax1.legend(loc='best')
    ax1.set_title('Competition Model using Euler: Varying N1')
    ax1.grid(True)

    # ---> RK8: Varying N1
    ax2.plot(time_R_Q2_N1, N2_R_Q2_N1, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax2.set_ylim(-0.25,1.5)
    ax2.set_xlim(0, 25)
    ax2.set_ylabel('Population/Carrying Cap.')
    # ax2.legend(loc='best')
    ax2.set_title('Competition Model using RK8: Varying N1')
    ax2.grid(True)

    # ---> Euler: Varying N2
    ax3.plot(time_E_Q2_N2, N1_E_Q2_N2, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax3.set_ylim(-0.25,1.5)
    ax3.set_xlim(0, 25)
    ax3.set_xlabel('Time (years)')
    ax3.set_ylabel('Population/Carrying Cap.')
    # ax3.legend(loc='best')
    ax3.set_title('Competition Model using Euler: Varying N2')
    ax3.grid(True)

    # ---> RK8: Varying N2
    ax4.plot(time_R_Q2_N2, N2_R_Q2_N2, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax4.set_ylim(-0.25,1.5)
    ax4.set_xlim(0, 25)
    ax4.set_xlabel('Time (years)')
    ax4.set_ylabel('Population/Carrying Cap.')
    ax4.set_title('Competition Model using RK8: Varying N2')
    ax4.legend(loc="best")
    ax4.grid(True)

fig1.suptitle("How do the initial conditions affect the final result and behavior of the two species?", fontsize=24)
fig1.text(0.5, 0.94, "Coefficients: a = 1, b = 2, c = 1, d = 3, Δt = 1.0", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig1.savefig("plot_lab2_3_Q2_f1_Competing_change_initialconditions.png")
plt.close()

#---------------------------------------------------------------
# 2-2: Varying coefficients
#---------------------------------------------------------------

# ------------> Set up the variables
coef_vary = np.arange(1,5,0.5)

# ------------------------------------Euler----------------------------------------
fig2, axs2 = plt.subplots(2, 2, figsize=(19, 11))
ax5, ax6, ax7, ax8 = axs2.ravel() 

for g in range(len(coef_vary)):
    # ------------> Varying coefficient "a"
    [time_E_Q2_a,N1_E_Q2_a,N2_E_Q2_a] = euler_solve(dNdt_comp, a = coef_vary[g], dt=1.0, t_final=21.0)

    # ------------> Varying coefficient "b"
    [time_E_Q2_b,N1_E_Q2_b,N2_E_Q2_b] = euler_solve(dNdt_comp, b = coef_vary[g], dt=1.0, t_final=21.0)

    # ------------> Varying coefficient "c"
    [time_E_Q2_c,N1_E_Q2_c,N2_E_Q2_c] = euler_solve(dNdt_comp, c = coef_vary[g], dt=1.0, t_final=21.0)
    
    # ------------> Varying coefficient "d"
    [time_E_Q2_d,N1_E_Q2_d,N2_E_Q2_d] = euler_solve(dNdt_comp, d = coef_vary[g], dt=1.0, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(coef_vary)))
    
    # ------------> Plot (Euler)

    # ---> Euler: Varying a
    ax5.plot(time_E_Q2_a, N1_E_Q2_a, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax5.set_ylim(-0.25,1.5)
    ax5.set_xlim(0, 25)
    ax5.set_ylabel('Population/Carrying Cap.')
    # ax5.legend(loc='best')
    ax5.set_title('Competition Model using Euler: Varying a')
    ax5.grid(True)

    # ---> Euler: Varying b
    ax6.plot(time_E_Q2_b, N1_E_Q2_b, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax6.set_ylim(-0.25,1.5)
    ax6.set_xlim(0, 25)
    ax6.set_ylabel('Population/Carrying Cap.')
    ax6.legend(loc='best')
    ax6.set_title('Competition Model using Euler: Varying b')
    ax6.grid(True)

    # ---> Euler: Varying c
    ax7.plot(time_E_Q2_c, N1_E_Q2_c, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax7.set_ylim(-0.25,1.5)
    ax7.set_xlim(0, 25)
    ax7.set_ylabel('Population/Carrying Cap.')
    ax7.set_xlabel('Time (years)')
    # ax7.legend(loc='best')
    ax7.set_title('Competition Model using Euler: Varying c')
    ax7.grid(True)

    # ---> Euler: Varying d
    ax8.plot(time_E_Q2_d, N1_E_Q2_d, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax8.set_ylim(-0.25,1.5)
    ax8.set_xlim(0, 25)
    ax8.set_ylabel('Population/Carrying Cap.')
    ax8.set_xlabel('Time (years)')
    # ax8.legend(loc='best')
    ax8.set_title('Competition Model using Euler: Varying d')
    ax8.grid(True)
fig2.suptitle("How do the coefficient values affect the final result and behavior of the two species using Euler Method?", fontsize=24)
fig2.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 1.0", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig2.savefig("plot_lab2_3_Q2_f2_Competing_change_coefficients_Euler.png")
plt.close()

#------------------------------------RK8---------------------------------------
fig3, axs3 = plt.subplots(2, 2, figsize=(19, 11))
ax9, ax10, ax11, ax12 = axs3.ravel() 

for k in range(len(coef_vary)):
    # ------------> Varying coefficient "a"
    [time_R_Q2_a,N1_R_Q2_a,N2_R_Q2_a] = solve_rk8(dNdt_comp, a = coef_vary[k], dt=1.0, t_final=21.0)

    # ------------> Varying coefficient "b"
    [time_R_Q2_b,N1_R_Q2_b,N2_R_Q2_b] = solve_rk8(dNdt_comp, b = coef_vary[k], dt=1.0, t_final=21.0)

    # ------------> Varying coefficient "c"
  
    [time_R_Q2_c,N1_R_Q2_c,N2_R_Q2_c] = solve_rk8(dNdt_comp, c = coef_vary[k], dt=1.0, t_final=21.0)
    
    # ------------> Varying coefficient "d"
    [time_R_Q2_d,N1_R_Q2_d,N2_R_Q2_d] = solve_rk8(dNdt_comp, d = coef_vary[k], dt=1.0, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(coef_vary)))
    
    # ------------> Plot (RK8)

    # ---> RK8: Varying a
    ax9.plot(time_R_Q2_a, N1_R_Q2_a, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax9.set_ylim(-0.25,1.5)
    ax9.set_xlim(0, 25)
    ax9.set_ylabel('Population/Carrying Cap.')
    # ax9.legend(loc='best')
    ax9.set_title('Competition Model using RK8: Varying a')
    ax9.grid(True)

    # ---> RK8: Varying b
    ax10.plot(time_R_Q2_b, N1_R_Q2_b, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax10.set_ylim(-0.25,1.5)
    ax10.set_xlim(0, 25)
    ax10.set_ylabel('Population/Carrying Cap.')
    ax10.legend(loc='best')
    ax10.set_title('Competition Model using RK8: Varying b')
    ax10.grid(True)

    # ---> RK8: Varying c
    ax11.plot(time_R_Q2_c, N1_R_Q2_c, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax11.set_ylim(-0.25,1.5)
    ax11.set_xlim(0, 25)
    ax11.set_ylabel('Population/Carrying Cap.')
    ax11.set_xlabel('Time (years)')
    # ax11.legend(loc='best')
    ax11.set_title('Competition Model using RK8: Varying c')
    ax11.grid(True)

    # ---> RK8: Varying d
    ax12.plot(time_R_Q2_d, N1_R_Q2_d, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax12.set_ylim(-0.25,1.5)
    ax12.set_xlim(0, 25)
    ax12.set_ylabel('Population/Carrying Cap.')
    ax12.set_xlabel('Time (years)')
    # ax12.legend(loc='best')
    ax12.set_title('Competition Model using RK8: Varying d')
    ax12.grid(True)
fig3.suptitle("How do the coefficient values affect the final result and behavior of the two species using RK8 Method?", fontsize=24)
fig3.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 1.0", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig3.savefig("plot_lab2_3_Q2_f3_Competing_change_coefficients_RK8.png")
plt.close()
# for i in range(10):
#     plt.plot(np.arange(5) + i)
#     plt.text(5,3.5+i,f"line#{i}")