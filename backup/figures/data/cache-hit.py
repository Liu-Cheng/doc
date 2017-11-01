#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 8))
fig.subplots_adjust(hspace=.5)
#=========================
# RPA cache
#========================
x1=(1, 2, 3, 4, 5, 6)
rpao_x_lable=('32b', '64b', '128b', '256b', '512b', '2x512b')
youtube_rpao_hit_rate   = (0.370, 0.579, 0.725, 0.824, 0.891, 0.934)
lj_rpao_hit_rate        = (0.307, 0.496, 0.656, 0.778, 0.861, 0.916)
pokec_rpao_hit_rate     = (0.242, 0.412, 0.590, 0.738, 0.840, 0.906)
rmat19_32_rpao_hit_rate = (0.211, 0.372, 0.557, 0.716, 0.826, 0.899)
rmat21_32_rpao_hit_rate = (0.180, 0.322, 0.504, 0.678, 0.808, 0.892)
ax1.set_title('RPA Read Cache')

ax1.plot(x1, youtube_rpao_hit_rate, '-<')
ax1.plot(x1, lj_rpao_hit_rate, '-s')
ax1.plot(x1, pokec_rpao_hit_rate, '->')
ax1.plot(x1, rmat19_32_rpao_hit_rate, '-^')
ax1.plot(x1, rmat21_32_rpao_hit_rate, '-p')
ax1.set_ylabel('Cache hit rate')
ax1.set_xticks(x1)
ax1.set_xticklabels(rpao_x_lable)
vals=ax1.get_yticks()
ax1.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax1.grid(linewidth=0.5)
ax1.xaxis.grid(False)

#==============================
# CIA Cache
#===============================
x2=(1, 2, 3, 4, 5, 6)
ciao_x_lable=('32b', '64b', '128b', '256b', '512b', '2x512b')
youtube_ciao_hit_rate   = (0.0600, 0.475, 0.718, 0.844, 0.912, 0.950)
lj_ciao_hit_rate        = (0.0028, 0.489, 0.734, 0.858, 0.922, 0.956)
pokec_ciao_hit_rate     = (0.0002, 0.489, 0.734, 0.857, 0.920, 0.954)
rmat19_32_ciao_hit_rate = (0.0002, 0.497, 0.746, 0.871, 0.934, 0.966)
rmat21_32_ciao_hit_rate = (0.0001, 0.496, 0.745, 0.869, 0.932, 0.964)
ax2.set_title('CIA Read Cache')

ax2.plot(x2, youtube_ciao_hit_rate, '-<')
ax2.plot(x2, lj_ciao_hit_rate, '-s')
ax2.plot(x2, pokec_ciao_hit_rate, '->')
ax2.plot(x2, rmat19_32_ciao_hit_rate, '-^')
ax2.plot(x2, rmat21_32_ciao_hit_rate, '-p')
ax2.set_ylabel('Cache hit rate')
ax2.set_xticks(x2)
ax2.set_xticklabels(ciao_x_lable)
vals=ax2.get_yticks()
ax2.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax2.grid(linewidth=0.5)
ax2.xaxis.grid(False)

#=========================
# Depth cache
#========================
x3=(1, 2, 3, 4, 5, 6)
depth_x_lable=('1K x 512b', '2K x 512b', '4K x 512b', '8K x 512b', '16K x 512b', '2 x 16K x 512b')
youtube_depth_hit_rate   = (0.649, 0.707, 0.791, 0.877, 0.953, 0.969)
lj_depth_hit_rate        = (0.374, 0.421, 0.481, 0.571, 0.703, 0.815)
pokec_depth_hit_rate     = (0.171, 0.241, 0.363, 0.579, 0.889, 0.991)
rmat19_32_depth_hit_rate = (0.123, 0.247, 0.496, 0.990, 0.990, 0.990)
rmat21_32_depth_hit_rate = (0.031, 0.062, 0.126, 0.255, 0.511, 0.994)
ax3.set_title('Depth Read/Write Cache')

ax3.plot(x3, youtube_depth_hit_rate, '-<')
ax3.plot(x3, lj_depth_hit_rate, '-s')
ax3.plot(x3, pokec_depth_hit_rate, '->')
ax3.plot(x3, rmat19_32_depth_hit_rate, '-^')
ax3.plot(x3, rmat21_32_depth_hit_rate, '-p')
ax3.set_ylabel('Cache hit rate')
ax3.set_xticks(x3)
ax3.set_xticklabels(depth_x_lable)
vals=ax3.get_yticks()
ax3.set_yticklabels(['{:3.1f}%'.format(100*x) for x in vals])
ax3.grid(linewidth=0.5)
ax3.xaxis.grid(False)
ax3.set_xlabel('Cache Size')


# Adding the legend and showing the plot
#ax1.legend(['youtube', 'lj', 'pokec', 'ramt-19-32', 'rmat-21-32'],
#        loc='lower right',
#        ncol=3)
ax2.legend(['youtube', 'lj', 'pokec', 'ramt-19-32', 'rmat-21-32'],
        loc='lower right',
        ncol=3)

#ax3.legend(['youtube', 'lj', 'pokec', 'ramt-19-32', 'rmat-21-32'],
#        loc='lower right',
#        ncol=3)

#=======================================================================

#ret.get_frame().set_alpha(0.4)
plt.savefig("../cache-hit.pdf", bbox_inches='tight')
#plt.show()
