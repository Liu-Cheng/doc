#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.style.use('default')
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

fig, ax = plt.subplots(1, figsize=(6, 4))
#=======================================================
# load balance of straightforward data path duplication
#=======================================================
x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
s0 = "0.00000   0.00000   0.50000   0.67500   0.79077   0.73805   0.40375   0.09700   0.01918   0.01112 0.00932   0.01355   0.00867   0.00000   0.00000"
s1 = "0.00000   0.66667   0.37500   0.18333   0.13416   0.17905   0.33120   0.24162   0.07138   0.04289 0.04257   0.04251   0.04335   0.03750   0.10000"
s2 = "0.00000   0.33333   0.00000   0.10833   0.06304   0.07255   0.21865   0.34031   0.14550   0.07335 0.05201   0.03697   0.02890   0.01250   0.00000"
s3 = "1.00000   0.00000   0.12500   0.03333   0.01203   0.01034   0.04640   0.32107   0.76394   0.87264 0.89610   0.90696   0.91907   0.95000   0.90000"
d0 = [float(i) for i in s0.split()]
d1 = [float(i) for i in s1.split()]
d2 = [float(i) for i in s2.split()]
d3 = [float(i) for i in s3.split()]

t0=[1, 0.33, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.3]
t1=[0, 0.33, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.3]
t2=[0, 0.33, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.2]
t3=[0, 0.00, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.2]

sim_DPD_2lanes_p0 = np.add(d0, d1)
sim_DPD_2lanes_p1 = np.add(d2, d3)

sim_DPD_4lanes_p0 = d0
sim_DPD_4lanes_p1 = d1
sim_DPD_4lanes_p2 = d2
sim_DPD_4lanes_p3 = d3

opt_DPD_2lanes_p0 = np.add(t0, t1)
opt_DPD_2lanes_p1 = np.add(t2, t3)

opt_DPD_4lanes_p0 = t0
opt_DPD_4lanes_p1 = t1
opt_DPD_4lanes_p2 = t2
opt_DPD_4lanes_p3 = t3

#ax.plot(x, sim_DPD_2lanes_p0, '-r<')
#ax.plot(x, sim_DPD_2lanes_p1, '-r<', label='_nolegend_')

ax.plot(x, sim_DPD_4lanes_p0, '-C0^')
ax.plot(x, sim_DPD_4lanes_p1, '-C0^', label='_nolegend_')
ax.plot(x, sim_DPD_4lanes_p2, '-C0^', label='_nolegend_')
ax.plot(x, sim_DPD_4lanes_p3, '-C0^', label='_nolegend_')

#ax.plot(x, opt_DPD_2lanes_p0, '-ys')
#ax.plot(x, opt_DPD_2lanes_p1, '-ys', label='_nolegend_')

ax.plot(x, opt_DPD_4lanes_p0, '-C1p')
ax.plot(x, opt_DPD_4lanes_p1, '-C1p', label='_nolegend_')
ax.plot(x, opt_DPD_4lanes_p2, '-C1p', label='_nolegend_')
ax.plot(x, opt_DPD_4lanes_p3, '-C1p', label='_nolegend_')

ax.set_xlabel('BFS iterations')
ax.set_ylabel('Frontier percentage')
vals=ax.get_yticks()
ax.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax.grid(linewidth=0.5)
ax.xaxis.grid(False)

ax.legend(['sim_4lanes', 'opt_4lanes'],
    loc='upper center',
    ncol=2)

plt.savefig("../load-balance.pdf", bbox_inches='tight')
