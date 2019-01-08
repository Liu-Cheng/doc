#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


hash_size=['16', '32', '2x16', '64', '4x16', '128', '8x16', '256', '16x16', '512', '32x16']
freq =[200, 190, 200, 160, 200, 140, 200, 130, 200, 100, 200]

# Setting the positions and width for the bars
width = 0.5
xdata = np.arange(len(freq))

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
ax.bar(xdata,
        freq,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        edgecolor='k',
        # with color
        color='silver',
        # with label the first value in first_name
        label=hash_size)

# Set the y axis label
ax.set_ylabel('Implementation Frequency (MHz)')
ax.set_xlabel('Hash Table Configurations (x1024 Entries)')

# Set the position of the x ticks
ax.set_xticks(xdata)

# Set the labels for the x ticks
ax.set_xticklabels(hash_size)

ax.grid(linewidth=0.5)
ax.xaxis.grid(False)


# Adding the legend and showing the plot
#plt.show()

plt.savefig("../hash-freq.pdf", bbox_inches='tight')
