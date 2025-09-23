#!/usr/bin/python3
'''
Series of simple examples for Lecture 3 about pray and predator problem

'''

import numpy as np
import matplotlib.pyplot as plt

dx = 0.1
x = np.arange(0, 6*np.pi, dx)
sinx = np.sin(x)
cosx = np.cos(x) # Analytical Solution!

#--------- The Hard Way!
#fwd_diff =np.zeros(x.size-1)
#for i in range(x.size-1):
#    fwd_diff[i] = x[i+1] - x[i]

#--------- The Easy Way!
fwd_diff = (sinx[1:]-sinx[:-1])/dx
bkd_diff = (sinx[1:]-sinx[:-1])/dx
cnt_diff = (sinx[2:] - sinx[:-2]) /(2*dx)

fig, ax = plt.subplots(1, 1)
ax.plot(x,cosx, label=r'Analytical Derivative of $\sin{x}$')
ax.plot(x[:-1],fwd_diff, label='Forward Diff Approx')
ax.plot(x[1:],bkd_diff, label='Backward Diff Approx')
ax.plot(x[1:-1],cnt_diff, label='Central Diff Approx')
ax.legend(loc='best')
fig.show()

#--------- Our dx values
err_fwd, err_cnt = [], []
dxs = [2**-n for n in range(10)]

for dx in dxs:
    x = np.arange(0, 2.5 * np.pi, dx)
    sinx = np.sin(x)

    fwd_diff = (sinx[1:] - sinx[:-1]) / dx
    cnt_diff = (sinx[2:] - sinx[:-2]) / (2*dx)

    err_fwd.append(np.abs(fwd_diff[-1] - np.cos(x[-1])))
    err_cnt.append(np.abs(cnt_diff[-1] - np.cos(x[-2])))

fig2, ax2 = plt.subplots(1, 1)
ax2.loglog(dxs, err_fwd, '.', label='Foward Diff')
ax2.loglog(dxs, err_cnt, '.', label='Central Diff')
ax2.set_xlabel(r'$\Delta x$')
ax2.set_ylabel('Error')
ax2.legend(loc='best')
fig2.show()
