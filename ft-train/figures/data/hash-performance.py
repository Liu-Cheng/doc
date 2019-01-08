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


#hash_size=[16, 32, 2x16, 64, 4x16, 128, 256, 512]
freq =[200, 190, 200, 160, 140, 130, 100]
base_runtime=[1.4022, 9.7264, 3.8728, 2.1245, 8.6928]
raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        'Hash-16K':  [1.4022/1.319, 9.7264/8.6736, 3.8728/3.6125, 2.1245/1.6139, 8.6928/6.4784],
        'Hash-32K':  [1.4022/1.337, 9.7264/8.6961, 3.8728/3.5858, 2.1245/1.6033, 8.6928/6.5133],
        'Hash-2x16K':  [1.4022/1.31254, 9.7264/8.5783, 3.8728/3.5432, 2.1245/1.5728, 8.6928/6.4223],
        'Hash-64K':  [1.4022/1.399, 9.7264/9.0397, 3.8728/3.6985, 2.1245/1.6263, 8.6928/6.6747],
        'Hash-4x16K':  [1.4022/1.30749, 9.7264/8.4916, 3.8728/3.4764, 2.1245/1.51867, 8.6928/6.31238],
        #'Hash-4x16K-visited':  [1.4022/1.29937, 9.7264/8.4595, 3.8728/3.4573, 2.1245/1.5056, 8.6928/6.2601],
        'Hash-128K': [1.4022/1.444, 9.7264/9.3436, 3.8728/3.7348, 2.1245/1.6379, 8.6928/6.8229],
        'Hash-8x16K': [1.4022/1.29985, 9.7264/8.40589, 3.8728/3.41282, 2.1245/1.47987, 8.6928/6.13179],
        'Hash-256K': [1.4022/1.478, 9.7264/9.5138, 3.8728/3.8259, 2.1245/1.6758, 8.6928/6.8369],
        'Hash-16x16K': [1.4022/1.2935, 9.7264/8.3127, 3.8728/3.35114, 2.1245/1.46585, 8.6928/5.92571],
        'Hash-512K': [1.4022/1.609, 9.7264/10.357, 3.8728/4.1191, 2.1245/1.8433, 8.6928/7.3853],
        'Hash-32x16K': [1.4022/1.2848, 9.7264/8.2213, 3.8728/3.28743, 2.1245/1.46271, 8.6928/5.8175]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'Hash-16K', 'Hash-32K', 'Hash-2x16K',
    'Hash-64K', 'Hash-4x16K', 'Hash-128K', 'Hash-8x16K', 'Hash-256K', 'Hash-16x16K',
    'Hash-512K', 'Hash-32x16K'])
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
#vals=ax.get_yticks()
#ax.set_yticklabels(['{:3.2f}%'.format(x) for x in vals])
ax.grid(linewidth=0.5)
ax.xaxis.grid(False)

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0.8, 1.5])

# Adding the legend and showing the plot
ret = plt.legend(['Hash-16K', 'Hash-32K', 'Hash-2x16K', 'Hash-64K', 'Hash-4x16K', 'Hash-128K', 'Hash-8x16K',
    'Hash-256K', 'Hash-16x16K', 'Hash-512K', 'Hash-32x16K'],
        loc='upper left',
        ncol=2)
ret.get_frame().set_alpha(0.4)
#bbox_to_anchor=(0.1, 0.3))
#plt.grid()
#plt.show()

plt.savefig("../hash-performance.pdf", bbox_inches='tight')
