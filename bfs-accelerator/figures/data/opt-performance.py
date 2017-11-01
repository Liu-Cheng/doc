#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#c1 baseline
#c2 pipelined
#c3 hash
#c4 prefetch
#c5 cache
#c6 data path duplication
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

raw_data = {'graph': ['Youtube', 'LJ', 'Pokec', 'R-MATI', 'R-MATII'],
        'c1': [16.1344/16.1344, 90.5813/90.5813, 32.1934/32.1934, 12.6965/12.6965, 50.7354/50.7354],
        'c2': [16.1344/1.40220, 90.5813/9.72640, 32.1934/3.87280, 12.6965/2.12450, 50.7354/8.69280],
        'c3': [16.1344/1.30749, 90.5813/8.49160, 32.1934/3.47640, 12.6965/1.51867, 50.7354/6.31238],
        'c4': [16.1344/0.62222, 90.5813/4.96700, 32.1934/2.29210, 12.6965/1.51867, 50.7354/3.14820],
        'c5': [16.1344/0.46200, 90.5813/4.33520, 32.1934/1.52970, 12.6965/0.66920, 50.7354/3.04120],
        'c6': [16.1344/0.20820, 90.5813/2.45990, 32.1934/1.05420, 12.6965/0.20420, 50.7354/2.41810]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
label=('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
# Setting the positions and width for the bars
pos = list(range(len(df['c1'])))
width = 0.12
ecolor='k'
lw=0.5
print pos

#cmap = plt.get_cmap('jet')
#colors = cmap(np.linspace(0, 1.0, len(fuck_label)))

# Plotting the bars
fig, ax = plt.subplots(figsize=(6,4))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['c1'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        hatch=4*'/',
        # with alpha 0.5
        alpha=0.3,
        # with color
        #color=colors[0],
        color='w',
        # with label the first value in first_name
        label=label[0])

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['c2'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.3,
        # with color
        linewidth=lw,
        edgecolor='k',
        hatch=4*'.',
        color='w',
        #color=colors[1],
        # with label the second value in first_name
        label=label[1])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['post_score'] data,
        df['c3'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        # with alpha 0.5
        alpha=0.3,
        # with color
        hatch=2*'-',
        color='w',
        #color=colors[2],
        # with label the third value in first_name
        label=label[2])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        #using df['post_score'] data,
        df['c4'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        # with alpha 0.5
        alpha=0.3,
        # with color
        #color=colors[3],
        hatch=4*'\\',
        color='w',
        # with label the third value in first_name
        label=label[3])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],
        #using df['post_score'] data,
        df['c5'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        # with alpha 0.5
        alpha=0.3,
        # with color
        #color=colors[3],
        hatch=2*'o',
        color='w',
        # with label the third value in first_name
        label=label[4])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos],
        #using df['post_score'] data,
        df['c6'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        # with alpha 0.5
        alpha=0.3,
        # with color
        #color=colors[3],
        hatch=2*'+',
        color='w',
        # with label the third value in first_name
        label=label[5])


# Set the y axis label
ax.set_ylabel('Normalized Performance')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 3 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5'] + df['c6'] + df['c7'] + df['c8'] + df['c9'])] )

# Adding the legend and showing the plot
plt.legend(['baseline', '+pipeline', '+hash filter', '+prefetch', '+cache', '+duplicate path'], ncol=2, loc='upper center')
ax.grid(linewidth='0.5')
ax.xaxis.grid(False)
#plt.show()

plt.savefig("../opt-performance.pdf", bbox_inches='tight')
