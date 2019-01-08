#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

fig, (ax3, ax4) = plt.subplots(2, figsize=(6, 5))
fig.subplots_adjust(hspace=.5)
#=========================
# RPA cache
#========================
#x1=(1, 2, 3, 4, 5, 6)
#rpao_x_lable=('4B', '8B', '16B', '32B', '64B', '128B')
#youtube_rpao_hit_rate   = (0.370, 0.579, 0.725, 0.824, 0.891, 0.934)
#lj_rpao_hit_rate        = (0.307, 0.496, 0.656, 0.778, 0.861, 0.916)
#pokec_rpao_hit_rate     = (0.242, 0.412, 0.590, 0.738, 0.840, 0.906)
#rmat19_32_rpao_hit_rate = (0.211, 0.372, 0.557, 0.716, 0.826, 0.899)
#rmat21_32_rpao_hit_rate = (0.180, 0.322, 0.504, 0.678, 0.808, 0.892)
#ax1.set_title('RPA prefetch buffer')
#
#ax1.plot(x1, youtube_rpao_hit_rate, '-<')
#ax1.plot(x1, lj_rpao_hit_rate, '-s')
#ax1.plot(x1, pokec_rpao_hit_rate, '->')
#ax1.plot(x1, rmat19_32_rpao_hit_rate, '-^')
#ax1.plot(x1, rmat21_32_rpao_hit_rate, '-p')
#ax1.set_ylabel('Hit rate')
#ax1.set_xticks(x1)
#ax1.set_xticklabels(rpao_x_lable)
#vals=ax1.get_yticks()
#ax1.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
#ax1.grid(linewidth=0.5)
#ax1.xaxis.grid(False)
#
##==============================
## CIA Cache
##===============================
#x2=(1, 2, 3, 4, 5, 6)
#ciao_x_lable=('4B', '8B', '16B', '32B', '64B', '128B')
#youtube_ciao_hit_rate   = (0.0600, 0.475, 0.718, 0.844, 0.912, 0.950)
#lj_ciao_hit_rate        = (0.0028, 0.489, 0.734, 0.858, 0.922, 0.956)
#pokec_ciao_hit_rate     = (0.0002, 0.489, 0.734, 0.857, 0.920, 0.954)
#rmat19_32_ciao_hit_rate = (0.0002, 0.497, 0.746, 0.871, 0.934, 0.966)
#rmat21_32_ciao_hit_rate = (0.0001, 0.496, 0.745, 0.869, 0.932, 0.964)
#ax2.set_title('CIA prefetch buffer')
#
#ax2.plot(x2, youtube_ciao_hit_rate, '-<')
#ax2.plot(x2, lj_ciao_hit_rate, '-s')
#ax2.plot(x2, pokec_ciao_hit_rate, '->')
#ax2.plot(x2, rmat19_32_ciao_hit_rate, '-^')
#ax2.plot(x2, rmat21_32_ciao_hit_rate, '-p')
#ax2.set_ylabel('Hit rate')
#ax2.set_xticks(x2)
#ax2.set_xticklabels(ciao_x_lable)
#vals=ax2.get_yticks()
#ax2.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
#ax2.grid(linewidth=0.5)
#ax2.xaxis.grid(False)

#=========================
# Depth read cache
#========================
fig.subplots_adjust(hspace=.6)
x3=(1, 2, 3, 4, 5, 6, 7)
depth_x_lable=('1Kx64B', '2Kx64B', '4Kx64B', '8Kx64B', '16Kx64B', '32Kx64B', '64Kx64B')
youtube_depth_read_rate   = (0.57, 0.65, 0.75, 0.86, 0.95, 0.97, 0.97)
lj_depth_read_rate        = (0.35, 0.40, 0.46, 0.56, 0.70, 0.86, 0.99)
pokec_depth_read_rate     = (0.16, 0.23, 0.35, 0.57, 0.89, 0.99, 0.99)
rmat19_32_depth_read_rate = (0.12, 0.25, 0.50, 0.99, 0.99, 0.99, 0.99)
rmat21_32_depth_read_rate = (0.03, 0.06, 0.13, 0.26, 0.51, 0.99, 0.99)
ax3.set_title('Depth read cache')

ax3.plot(x3, youtube_depth_read_rate, '-<')
ax3.plot(x3, lj_depth_read_rate, '-s')
ax3.plot(x3, pokec_depth_read_rate, '->')
ax3.plot(x3, rmat19_32_depth_read_rate, '-^')
ax3.plot(x3, rmat21_32_depth_read_rate, '-p')
ax3.set_ylabel('Hit rate')
ax3.set_xticks(x3)
ax3.set_xticklabels(depth_x_lable)
for tick in ax3.get_xticklabels():
    tick.set_rotation(15)


vals=ax3.get_yticks()
ax3.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax3.grid(linewidth=0.5)
ax3.xaxis.grid(False)

#=========================
# Depth write cache
#========================
x4=(1, 2, 3, 4, 5, 6, 7)
depth_x_lable=('1Kx64B', '2Kx64B', '4Kx64B', '8Kx64B', '16Kx64B', '32Kx64B', '64Kx64B')
youtube_depth_write_rate   = (0.73, 0.77, 0.84, 0.91, 0.98, 0.99, 0.99)
lj_depth_write_rate        = (0.40, 0.44, 0.49, 0.57, 0.70, 0.87, 0.99)
pokec_depth_write_rate     = (0.20, 0.26, 0.37, 0.58, 0.88, 0.99, 0.99)
rmat19_32_depth_write_rate = (0.12, 0.25, 0.50, 0.99, 0.99, 0.99, 0.99)
rmat21_32_depth_write_rate = (0.03, 0.06, 0.13, 0.26, 0.51, 0.99, 0.99)
ax4.set_title('Depth write cache')

ax4.plot(x4, youtube_depth_write_rate, '-<')
ax4.plot(x4, lj_depth_write_rate, '-s')
ax4.plot(x4, pokec_depth_write_rate, '->')
ax4.plot(x4, rmat19_32_depth_write_rate, '-^')
ax4.plot(x4, rmat21_32_depth_write_rate, '-p')
ax4.set_ylabel('Hit rate')
ax4.set_xticks(x4)
ax4.set_xticklabels(depth_x_lable)
vals=ax4.get_yticks()
ax4.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax4.grid(linewidth=0.5)
ax4.xaxis.grid(False)
ax4.set_xlabel('Cache Size')
for tick in ax4.get_xticklabels():
    tick.set_rotation(15)


# Adding the legend and showing the plot
#ax1.legend(['youtube', 'lj', 'pokec', 'ramt-19-32', 'rmat-21-32'],
#        loc='lower right',
#        ncol=3)
ax3.legend(['Youtube', 'LJ', 'Pokec', 'R-MATI', 'R-MATII'],
        loc='lower right',
        ncol=3)

#ax3.legend(['youtube', 'lj', 'pokec', 'ramt-19-32', 'rmat-21-32'],
#        loc='lower right',
#        ncol=3)

#=======================================================================

#ret.get_frame().set_alpha(0.4)
plt.savefig("../cache-hit.pdf", bbox_inches='tight')
#plt.show()
