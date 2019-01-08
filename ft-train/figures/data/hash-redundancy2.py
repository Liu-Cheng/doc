#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

xlabel = ('Youtube', 'LJ', 'Pokec', 'R-MATI', 'R-MATII')
hash_16K =   (37.856, 32.94,  15.897, 46.927, 29.432)
hash_32K =   (43.638, 36.454, 20.594, 59.586, 40.099)
hash_64K =   (50.023, 40.722, 27.455, 72.192, 52.049)
hash_128K =  (56.734, 46.386, 37.499, 82.962, 64.302)
hash_256K =  (63.300, 52.975, 51.363, 91.060, 75.758)
hash_512K =  (67.604, 61.359, 68.470, 96.326, 85.312)
hash_1024K = (69.952, 71.616, 84.000, 96.329, 92.321)
hash_2048K = (70.424, 80.608, 88.079, 96.329, 96.809)
hash_4096K = (70.424, 86.276, 88.079, 96.329, 96.809)
hash_8192K = (70.424, 86.518, 88.079, 96.329, 96.809)

xdata = (16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192)

youtube_rate = (hash_16K[0], hash_32K[0], hash_64K[0], hash_128K[0],
        hash_256K[0], hash_512K[0], hash_1024K[0], hash_2048K[0],
        hash_4096K[0], hash_8192K[0])

lj_rate = (hash_16K[1], hash_32K[1], hash_64K[1], hash_128K[1],
        hash_256K[1], hash_512K[1], hash_1024K[1], hash_2048K[1],
        hash_4096K[1], hash_8192K[1])

pokec_rate=(hash_16K[2], hash_32K[2], hash_64K[2], hash_128K[2],
        hash_256K[2], hash_512K[2], hash_1024K[2], hash_2048K[2],
        hash_4096K[2], hash_8192K[2])

rmat19_rate=(hash_16K[3], hash_32K[3], hash_64K[3], hash_128K[3],
        hash_256K[3], hash_512K[3], hash_1024K[3], hash_2048K[3],
        hash_4096K[3], hash_8192K[3])

rmat21_rate=(hash_16K[4], hash_32K[4], hash_64K[4], hash_128K[4],
        hash_256K[4], hash_512K[4], hash_1024K[4], hash_2048K[4],
        hash_4096K[4], hash_8192K[4])

#improve_16K = [0] * len(xdata)
#improve_32K = [0] * len(xdata)
#improve_64K = [0] * len(xdata)
#improve_128K = [0] * len(xdata)
#improve_256K = [0] * len(xdata)
#for i in range(0, len(xdata)):
#    improve_16K[i] = hash_32K[i] - hash_16K[i]
#    improve_32K[i] = hash_64K[i] - hash_32K[i]
#    improve_64K[i] = hash_128K[i] - hash_64K[i]
#    improve_128K[i] = hash_256K[i] - hash_128K[i]
#    improve_256K[i] = hash_512K[i] - hash_256K[i]
#
#youtube_improve_rate = [0] * len(xdata)
#lj_improve_rate = [0] * len(xdata)
#pokec_improve_rate = [0] * len(xdata)
#rmat19_improve_rate = [0] * len(xdata)
#rmat21_improve_rate = [0] * len(xdata)
#
#youtube_improve_rate[0] = improve_16K[0]/16.0
#youtube_improve_rate[1] = improve_32K[0]/32.0
#youtube_improve_rate[2] = improve_64K[0]/64.0
#youtube_improve_rate[3] = improve_128K[0]/128.0
#youtube_improve_rate[4] = improve_256K[0]/256.0
#
#lj_improve_rate[0] = improve_16K[1]/16.0
#lj_improve_rate[1] = improve_32K[1]/32.0
#lj_improve_rate[2] = improve_64K[1]/64.0
#lj_improve_rate[3] = improve_128K[1]/128.0
#lj_improve_rate[4] = improve_256K[1]/256.0
#
#pokec_improve_rate[0] = improve_16K[2]/16.0
#pokec_improve_rate[1] = improve_32K[2]/16.0
#pokec_improve_rate[2] = improve_64K[2]/16.0
#pokec_improve_rate[3] = improve_128K[2]/16.0
#pokec_improve_rate[4] = improve_256K[2]/16.0
#
#rmat19_improve_rate[0] = improve_16K[3]/16.0
#rmat19_improve_rate[1] = improve_32K[3]/16.0
#rmat19_improve_rate[2] = improve_64K[3]/16.0
#rmat19_improve_rate[3] = improve_128K[3]/16.0
#rmat19_improve_rate[4] = improve_256K[3]/16.0
#
#rmat21_improve_rate[0] = improve_16K[4]/16.0
#rmat21_improve_rate[1] = improve_32K[4]/16.0
#rmat21_improve_rate[2] = improve_64K[4]/16.0
#rmat21_improve_rate[3] = improve_128K[4]/16.0
#rmat21_improve_rate[4] = improve_256K[4]/16.0
#
# Plotting the bars
fig, ax = plt.subplots(figsize=(6,3))
ax.plot(xdata, youtube_rate, '-^')
ax.plot(xdata, lj_rate, '-s')
ax.plot(xdata, pokec_rate, '->')
ax.plot(xdata, rmat19_rate, '-<')
ax.plot(xdata, rmat21_rate, '-o')

# Set the y axis label
ax.set_ylabel('Redundancy removal rate')
ax.set_xlabel('Hash table size (KB)')
vals=ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x) for x in vals])
ax.grid(linewidth=0.5)
ax.xaxis.grid(False)

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0.6, 1.5])

# Adding the legend and showing the plot
ret = plt.legend(['Youtube', 'LJ', 'Pokec', 'R-MATI', 'R-MATII'],
        loc='lower right',
        ncol=2)
ret.get_frame().set_alpha(0.4)
#bbox_to_anchor=(0.1, 0.3))
#plt.grid()
plt.savefig("../hash-redundancy.pdf", bbox_inches='tight')

plt.show()
