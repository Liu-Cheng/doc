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


#hash_size=[16, 32, 64, 128, 256, 512]
#freq =[200, 190, ]
raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        'Hash-16K': [37.856, 32.94, 15.897, 46.927, 29.432],
        'Hash-32K': [43.638, 36.454, 20.594, 59.586, 40.099],
        'Hash-2x16K': [43.794,36.669, 20.644, 62.129, 41.238],
        'Hash-64K': [50.023, 40.722, 27.455, 72.192, 52.049],
        'Hash-4x16K': [50.239, 41.302, 27.557, 76.571, 54.652],
        #'Hash-4x16K-visited-1x16K': [53.349, 41.916, 29.166, 79.286, 56.035],
        'Hash-128K': [56.734, 46.386, 37.499, 82.962, 64.302],
        #'Hash-4x16K-visited-4x16K': [56.146, 44.254, 34.104, 85.135, 66.008],
        'Hash-8x16K': [56.802, 46.922, 37.686, 87.944, 68.526],
        'Hash-256K': [63.3, 52.975, 51.363, 91.06, 75.758],
        'Hash-16x16K': [62.457, 53.638, 51.729, 93.737, 81.091],
        'Hash-512K': [67.604, 61.359, 68.47, 96.326, 85.312],
        'Hash-32x16K': [66.269, 61.919, 68.336, 95.395, 90.359]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'Hash-16K', 'Hash-32K',
    'Hash-2x16K', 'Hash-64K', 'Hash-4x16K', 'Hash-128K', 'Hash-8x16K',
    'Hash-256K', 'Hash-16x16K', 'Hash-512K', 'Hash-32x16K'])
label=('Hash-16K', 'Hash-32K', 'Hash-2x16K', 'Hash-64K', 'Hash-4x16K',
        'Hash-128K', 'Hash-8x16K', 'Hash-256K', 'Hash-16x16K', 'Hash-512K', 'Hash-32x16K')

# Setting the positions and width for the bars
pos = list(range(len(df['Hash-16K'])))
width = 0.07
ecolor='k'
lw=0.5
print pos

#cmap = plt.get_cmap('jet')
#colors = cmap(np.linspace(0, 1.0, len(label)))

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['Hash-16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        hatch=4*'/',
        # with color
        color='chocolate',
        # with label the first value in first_name
        label=label[0])

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['Hash-32K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        hatch=4*'.',
        # with color
        color='r',
        # with label the second value in first_name
        label=label[1])

plt.bar([p + 2*width for p in pos],
        #using df['mid_score'] data,
        df['Hash-2x16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        hatch=2*'o',
        # with color
        color='r',
        # with label the second value in first_name
        label=label[2])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        #using df['post_score'] data,
        df['Hash-64K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        hatch=4*'x',
        # with label the third value in first_name
        label=label[3])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],
        #using df['post_score'] data,
        df['Hash-4x16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        hatch=4*'O',
        # with label the third value in first_name
        label=label[4])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos],
        #using df['post_score'] data,
        df['Hash-128K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='y',
        hatch=4*'-',
        # with label the third value in first_name
        label=label[5])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*6 for p in pos],
        #using df['post_score'] data,
        df['Hash-8x16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='y',
        hatch=4*'+',
        # with label the third value in first_name
        label=label[6])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*7 for p in pos],
        #using df['post_score'] data,
        df['Hash-256K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='g',
        hatch=4*'\\',
        # with label the third value in first_name
        label=label[7])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*8 for p in pos],
        #using df['post_score'] data,
        df['Hash-16x16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='g',
        hatch=2*'*',
        # with label the third value in first_name
        label=label[8])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*9 for p in pos],
        #using df['post_score'] data,
        df['Hash-512K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='c',
        hatch=2*'-',
        # with label the third value in first_name
        label=label[9])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*10 for p in pos],
        #using df['post_score'] data,
        df['Hash-32x16K'],
        # of width
        width,
        linewidth = lw,
        edgecolor = ecolor,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='c',
        hatch=2*'/',
        # with label the third value in first_name
        label=label[10])


# Set the y axis label
ax.set_ylabel('Normalized Performance')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])
vals=ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x) for x in vals])
ax.grid(linewidth=0.5)
ax.xaxis.grid(False)

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0.6, 1.5])

# Adding the legend and showing the plot
ret = plt.legend(['Hash-16K', 'Hash-32K', 'Hash-2x16K', 'Hash-64K', 'Hash-4x16K', 'Hash-128K', 'Hash-8x16K',
    'Hash-256K', 'Hash-16x16K', 'Hash-512K', 'Hash-32x16K'],
        loc='upper left',
        ncol=3)
ret.get_frame().set_alpha(0.4)
#bbox_to_anchor=(0.1, 0.3))
#plt.grid()
#plt.show()

plt.savefig("../hash-redundancy.pdf", bbox_inches='tight')
