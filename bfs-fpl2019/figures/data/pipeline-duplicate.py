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

base_runtime=[1.4022, 9.7264, 3.8728, 2.1245, 8.6928]
raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        '2-pipeline-baseline': [1.19384, 9.46781, 4.02860, 2.21747, 8.83400],
        '2-pipeline-balanced': [1.14972, 9.98414, 4.28803, 2.21594, 8.82374],
        '3-pipeline-baseline': [1.15480, 9.67210, 4.16424, 2.22288, 8.87396],
        '3-pipeline-balanced': [67.604, 61.359, 68.470, 96.326, 85.312]
        }
df = pd.DataFrame(raw_data, columns = ['graph', '2-pipeline-baseline', '2-pipeline-balanced', '3-pipeline-baseline', '3-pipeline-balanced'])
label=('2-pipeline-baseline', '2-pipeline-balanced', '3-pipeline-base', '3-pipeline-balanced')
# Setting the positions and width for the bars
pos = list(range(len(df['1-pipeline'])))
width = 0.1
ecolor='k'
lw=0.5
print pos

#cmap = plt.get_cmap('jet')
#colors = cmap(np.linspace(0, 1.0, len(label)))

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['2-pipeline-baseline'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        hatch=4*'.',
        # with color
        color='w',
        # with label the second value in first_name
        label=label[0])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['post_score'] data,
        df['2-pipeline-balanced'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='w',
        hatch=4*'x',
        # with label the third value in first_name
        label=label[1])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        #using df['post_score'] data,
        df['3-pipeline-baseline'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='w',
        hatch=4*'-',
        # with label the third value in first_name
        label=label[2])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],
        #using df['post_score'] data,
        df['3-baseline-balanced'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='w',
        hatch=4*'o',
        # with label the third value in first_name
        label=label[3])


# Set the y axis label
ax.set_ylabel('Normalized Performance')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 3 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])
#vals=ax.get_yticks()
#ax.set_yticklabels(['{:3.2f}%'.format(x) for x in vals])
ax.grid(linewidth=0.5)
ax.xaxis.grid(False)

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5'] + df['c6'] + df['c7'] + df['c8'] + df['c9'])] )

# Adding the legend and showing the plot
plt.legend(['2-pipeline-base', '2-pipeline-balanced', '4-pipeline-base', '4-pipeline-balanced'],
        loc='upper left',
        ncol=2)
#bbox_to_anchor=(0.1, 0.3))
#plt.grid()
#plt.show()

plt.savefig("../pipeline-duplicate.pdf", bbox_inches='tight')
