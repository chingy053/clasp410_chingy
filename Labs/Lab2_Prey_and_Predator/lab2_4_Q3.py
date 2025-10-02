#!/usr/bin/python3
'''
This file solve Question 3 (prompt as shown below) from Lab 2 and produce the plots.

Question 3: Focus on the Predator-Prey equations. Vary initial conditions and the different coefficients. In addition to making plots of population versus time, create plots with the prey species population on the x-axis and the predator species population on the y-axis. These are called phase diagrams, and can illustrate regular and irregular behavior. Answer the question, How do the initial conditions and coefficient values affect the final result and general behavior of the two species? Describe in qualitative terms, but provide examples. Carefully consider your phase diagrams. What new information did you gain from them?

Plot : time versus population to see how N1 and N2 change over time.
Plot : the prey species population on the x-axis and the predator species population on the y-axis
'''
#---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from lab2_1_functions import dNdt_pypdt, dNdt_comp, euler_solve, solve_rk8

#---------------------------------------------------------------
# 3-1: Varying initial conditions
#---------------------------------------------------------------

# ------------> Set up the variables
init_cond = np.arange(0.1,1.0,0.1)

fig1, axs1 = plt.subplots(2, 2, figsize=(19, 11))
ax1, ax2, ax3, ax4 = axs1.ravel() 

for i in range(len(init_cond)):
    # ------------> Varying N1 initial condition
    [time_E_Q3_N1,N1_E_Q3_N1,N2_E_Q3_N1] = euler_solve(dNdt_pypdt, N1_init=init_cond[i], dt=0.05, t_final=21.0)
    [time_R_Q3_N1,N1_R_Q3_N1,N2_R_Q3_N1] = solve_rk8(dNdt_pypdt,N1_init=init_cond[i], dt=0.05, t_final=21.0)

    # ------------> Varying N2 initial condition
    [time_E_Q3_N2,N1_E_Q3_N2,N2_E_Q3_N2] = euler_solve(dNdt_pypdt, N2_init=init_cond[i], dt=0.05, t_final=21.0)
    [time_R_Q3_N2,N1_R_Q3_N2,N2_R_Q3_N2] = solve_rk8(dNdt_pypdt,N2_init=init_cond[i], dt=0.05, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(init_cond)))
    # ------------> Plot

    # ---> Euler: Varying N1
    ax1.plot(time_E_Q3_N1, N1_E_Q3_N1, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax1.set_ylim(-0.25,2.0)
    ax1.set_xlim(0, 40)
    ax1.set_ylabel('Population/Carrying Cap.')
    # ax1.legend(loc='best')
    ax1.set_title('Predator-Prey Model using Euler: Varying N1')
    ax1.grid(True)

    # ---> RK8: Varying N1
    ax2.plot(time_R_Q3_N1, N2_R_Q3_N1, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax2.set_ylim(-0.25,2.0)
    ax2.set_xlim(0, 40)
    ax2.set_ylabel('Population/Carrying Cap.')
    # ax2.legend(loc='best')
    ax2.set_title('Predator-Prey Model using RK8: Varying N1')
    ax2.grid(True)

    # ---> Euler: Varying N2
    ax3.plot(time_E_Q3_N2, N1_E_Q3_N2, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax3.set_ylim(-0.25,2.0)
    ax3.set_xlim(0, 40)
    ax3.set_xlabel('Time (years)')
    ax3.set_ylabel('Population/Carrying Cap.')
    # ax3.legend(loc='best')
    ax3.set_title('Predator-Prey Model using Euler: Varying N2')
    ax3.grid(True)

    # ---> RK8: Varying N2
    ax4.plot(time_R_Q3_N2, N2_R_Q3_N2, color = def_colors[i], linewidth=2, label = f'Initial Population = {init_cond[i]:.2f}')
    ax4.set_ylim(-0.25,2.0)
    ax4.set_xlim(0, 40)
    ax4.set_xlabel('Time (years)')
    ax4.set_ylabel('Population/Carrying Cap.')
    ax4.set_title('Predator-Prey Model using RK8: Varying N2')
    ax4.legend(loc="best")
    ax4.grid(True)

fig1.suptitle("How do the initial conditions affect the final result and behavior of the two species?", fontsize=24)
fig1.text(0.5, 0.94, "Coefficients: a = 1, b = 2, c = 1, d = 3, Δt = 1.0", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig1.savefig("plot_lab2_4_Q3_f1_Predatorprey_change_initialconditions.png")
plt.close()

#---------------------------------------------------------------
# 4-2: Varying coefficients
#---------------------------------------------------------------

# ------------> Set up the variables
coef_vary = np.arange(1,5,0.5)

# ------------------------------------Euler----------------------------------------
fig2, axs2 = plt.subplots(2, 2, figsize=(19, 11))
ax5, ax6, ax7, ax8 = axs2.ravel() 

fig5, axs5 = plt.subplots(2, 2, figsize=(19, 11))
ax17, ax18, ax19, ax20 = axs5.ravel() 

for g in range(len(coef_vary)):
    # ------------> Varying coefficient "a"
    [time_E_Q3_a,N1_E_Q3_a,N2_E_Q3_a] = euler_solve(dNdt_pypdt, a = coef_vary[g], dt=0.05, t_final=21.0)

    # ------------> Varying coefficient "b"
    [time_E_Q3_b,N1_E_Q3_b,N2_E_Q3_b] = euler_solve(dNdt_pypdt, b = coef_vary[g], dt=0.05, t_final=21.0)

    # ------------> Varying coefficient "c"
    [time_E_Q3_c,N1_E_Q3_c,N2_E_Q3_c] = euler_solve(dNdt_pypdt, c = coef_vary[g], dt=0.05, t_final=21.0)
    
    # ------------> Varying coefficient "d"
    [time_E_Q3_d,N1_E_Q3_d,N2_E_Q3_d] = euler_solve(dNdt_pypdt, d = coef_vary[g], dt=0.05, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(coef_vary)))
    
    # ------------> Plot (Euler)

    # ---> Euler: Varying a
    ax5.plot(time_E_Q3_a, N1_E_Q3_a, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax5.set_ylim(-0.25,2.0)
    ax5.set_xlim(0, 40)
    ax5.set_ylabel('Population/Carrying Cap.')
    # ax5.legend(loc='best')
    ax5.set_title('Predator-Prey Model using Euler: Varying a')
    ax5.grid(True)

    # ---> Euler: Varying b
    ax6.plot(time_E_Q3_b, N1_E_Q3_b, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax6.set_ylim(-0.25,2.0)
    ax6.set_xlim(0, 40)
    ax6.set_ylabel('Population/Carrying Cap.')
    ax6.legend(loc='best')
    ax6.set_title('Predator-Prey Model using Euler: Varying b')
    ax6.grid(True)

    # ---> Euler: Varying c
    ax7.plot(time_E_Q3_c, N1_E_Q3_c, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax7.set_ylim(-0.25,2.0)
    ax7.set_xlim(0, 40)
    ax7.set_ylabel('Population/Carrying Cap.')
    ax7.set_xlabel('Time (years)')
    # ax7.legend(loc='best')
    ax7.set_title('Predator-Prey Model using Euler: Varying c')
    ax7.grid(True)

    # ---> Euler: Varying d
    ax8.plot(time_E_Q3_d, N1_E_Q3_d, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax8.set_ylim(-0.25,2.0)
    ax8.set_xlim(0, 40)
    ax8.set_ylabel('Population/Carrying Cap.')
    ax8.set_xlabel('Time (years)')
    # ax8.legend(loc='best')
    ax8.set_title('Predator-Prey Model using Euler: Varying d')
    ax8.grid(True)

    #----------------------------Phase Diagram------------------------------
    # ---> Euler: Varying a
    ax17.plot(N1_E_Q3_a, N2_E_Q3_a, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax17.set_ylim(-0.25,4.0)
    ax17.set_xlim(0, 20)
    ax17.set_ylabel('Predator Population (N2)')
    # ax17.legend(loc='best')
    ax17.set_title('Predator-Prey Model using Euler: Varying a')
    ax17.legend(loc='best')
    ax17.grid(True)

    # ---> Euler: Varying b
    ax18.plot(N1_E_Q3_b, N2_E_Q3_b, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax18.set_ylim(-0.25,4.0)
    ax18.set_xlim(0, 1.5)
    ax18.set_ylabel('Predator Population (N2)')
    ax18.set_title('Predator-Prey Model using Euler: Varying b')
    ax18.grid(True)

    # ---> Euler: Varying c
    ax19.plot(N1_E_Q3_c, N2_E_Q3_c, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax19.set_ylim(-0.25,4.0)
    ax19.set_xlim(0, 12)
    ax19.set_xlabel('Prey Population (N1)')
    ax19.set_ylabel('Predator Population (N2)')
    # ax19.legend(loc='best')
    ax19.set_title('Predator-Prey Model using Euler: Varying c')
    ax19.grid(True)

    # ---> Euler: Varying d
    ax20.plot(time_E_Q3_d, N1_E_Q3_d, color = def_colors[g], linewidth=2, label = f'Coefficient = {coef_vary[g]:.2f}')
    ax20.set_ylim(-0.25,3.0)
    ax20.set_xlim(0, 25)
    ax20.set_xlabel('Prey Population (N1)')
    ax20.set_ylabel('Predator Population (N2)')
    # ax20.legend(loc='best')
    ax20.set_title('Predator-Prey Model using Euler: Varying d')
    ax20.grid(True)

fig2.suptitle("How do the coefficient values affect the final result and behavior of the two species using Euler Method?", fontsize=24)
fig2.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 0.05", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig2.savefig("plot_lab2_4_Q3_f2_Predatorprey_change_coefficients_Euler.png")
plt.close()

fig5.suptitle("How do the coefficient values affect the final result and behavior of the two species using Euler Method?", fontsize=24)
fig5.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 0.05", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig5.savefig("plot_lab2_4_Q3_f4_PhaseDiagram_Predatorprey_change_coefficients_Euler.png")
plt.close()

#------------------------------------RK8---------------------------------------
fig3, axs3 = plt.subplots(2, 2, figsize=(19, 11))
ax9, ax10, ax11, ax12 = axs3.ravel() 

fig4, axs4 = plt.subplots(2, 2, figsize=(19, 11))
ax13, ax14, ax15, ax16 = axs4.ravel() 

for k in range(len(coef_vary)):
    # ------------> Varying coefficient "a"
    [time_R_Q3_a,N1_R_Q3_a,N2_R_Q3_a] = solve_rk8(dNdt_pypdt, a = coef_vary[k], dt=0.05, t_final=21.0)

    # ------------> Varying coefficient "b"
    [time_R_Q3_b,N1_R_Q3_b,N2_R_Q3_b] = solve_rk8(dNdt_pypdt, b = coef_vary[k], dt=0.05, t_final=21.0)

    # ------------> Varying coefficient "c"
  
    [time_R_Q3_c,N1_R_Q3_c,N2_R_Q3_c] = solve_rk8(dNdt_pypdt, c = coef_vary[k], dt=0.05, t_final=21.0)
    
    # ------------> Varying coefficient "d"
    [time_R_Q3_d,N1_R_Q3_d,N2_R_Q3_d] = solve_rk8(dNdt_pypdt, d = coef_vary[k], dt=0.05, t_final=21.0)

    # ------------> Define colors for plotting
    def_colors = plt.cm.rainbow(np.linspace(0, 1, len(coef_vary)))
    
    # ------------> Plot (RK8)

    # ---> RK8: Varying a
    ax9.plot(time_R_Q3_a, N1_R_Q3_a, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax9.set_ylim(-0.25,2.0)
    ax9.set_xlim(0, 40)
    ax9.set_ylabel('Population/Carrying Cap.')
    # ax9.legend(loc='best')
    ax9.set_title('Predator-Prey Model using RK8: Varying a')
    ax9.grid(True)

    # ---> RK8: Varying b
    ax10.plot(time_R_Q3_b, N1_R_Q3_b, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax10.set_ylim(-0.25,2.0)
    ax10.set_xlim(0, 40)
    ax10.set_ylabel('Population/Carrying Cap.')
    ax10.legend(loc='best')
    ax10.set_title('Predator-Prey Model using RK8: Varying b')
    ax10.grid(True)

    # ---> RK8: Varying c
    ax11.plot(time_R_Q3_c, N1_R_Q3_c, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax11.set_ylim(-0.25,2.0)
    ax11.set_xlim(0, 40)
    ax11.set_ylabel('Population/Carrying Cap.')
    ax11.set_xlabel('Time (years)')
    # ax11.legend(loc='best')
    ax11.set_title('Predator-Prey Model using RK8: Varying c')
    ax11.grid(True)

    # ---> RK8: Varying d
    ax12.plot(time_R_Q3_d, N1_R_Q3_d, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    ax12.set_ylim(-0.25,2.0)
    ax12.set_xlim(0, 40)
    ax12.set_ylabel('Population/Carrying Cap.')
    ax12.set_xlabel('Time (years)')
    # ax12.legend(loc='best')
    ax12.set_title('Predator-Prey Model using RK8: Varying d')
    ax12.grid(True)

    #----------------------------Phase Diagram------------------------------
    # ---> RK8: Varying a
    ax13.plot(N1_R_Q3_a, N2_R_Q3_a, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    # ax13.set_ylim(-0.25,2.0)
    # ax13.set_xlim(0, 40)
    ax13.set_ylabel('Predator Population (N2)')
    # ax13.legend(loc='best')
    ax13.set_title('Predator-Prey Model using RK8: Varying a')
    ax13.grid(True)

    # ---> RK8: Varying b
    ax14.plot(N1_R_Q3_b, N2_R_Q3_b, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    # ax14.set_ylim(-0.25,2.0)
    # ax14.set_xlim(0, 40)
    ax14.set_ylabel('Predator Population (N2)')
    # ax14.legend(loc='best')
    ax14.set_title('Predator-Prey Model using RK8: Varying b')
    ax14.grid(True)

    # ---> RK8: Varying c
    ax15.plot(N1_R_Q3_c, N2_R_Q3_c, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    # ax15.set_ylim(-0.25,2.0)
    # ax15.set_xlim(0, 40)
    ax15.set_ylabel('Predator Population (N2)')
    ax15.set_xlabel('Prey Population (N1)')
    # ax15.legend(loc='best')
    ax15.set_title('Predator-Prey Model using RK8: Varying c')
    ax15.grid(True)

    # ---> RK8: Varying d
    ax16.plot(N1_R_Q3_d, N2_R_Q3_d, color = def_colors[k], linewidth=2, label = f'Coefficient = {coef_vary[k]:.2f}')
    # ax16.set_ylim(-0.25,2.0)
    # ax16.set_xlim(0, 40)
    ax16.set_ylabel('Predator Population (N2)')
    ax15.set_xlabel('Prey Population (N1)')
    # ax16.legend(loc='best')
    ax16.set_title('Predator-Prey Model using RK8: Varying d')
    ax16.grid(True)
    ax16.legend(loc='best')
fig3.suptitle("How do the coefficient values affect the final result and behavior of the two species using RK8 Method?", fontsize=24)
fig3.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 0.05", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig3.savefig("plot_lab2_4_Q3_f3_Predatorprey_change_coefficients_RK8.png")
plt.close()

fig4.suptitle("How do the coefficient values affect the final result and behavior of the two species using RK8 Method?", fontsize=24)
fig4.text(0.5, 0.94, "Initial N1 = 0.5, Initial N2 = 0.5, Δt = 0.05", ha='center', va='top', fontsize=16)
plt.rcParams.update({'font.size': 16})
fig4.savefig("plot_lab2_4_Q3_f5_PhaseDiagram_Predatorprey_change_coefficients_RK8.png")
plt.close()




