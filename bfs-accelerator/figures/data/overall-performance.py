#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#c1 S3(cache)
#c2 S3(cache) + S4(cache) + S5(cache)
#c3 S2(cache) + S3(cache) + S4(cache) + S5(cache)
#c4 S3(cache) + S4-5(cache)
#C5 S2(cache) + S3(cache) + S4-5(cache)
#C6 S2(cache) + S3(cache) + S4-5(2 way cache)

raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        'baseline':  [16.1344/16.1344, 90.5813/90.5813, 32.1934/32.1934, 12.6965/12.6965, 50.7354/50.7354],
        #'this work':  [16.1344/0.3037, 90.5813/2.602, 32.1934/0.829, 12.6965/0.3594, 50.7354/2.0541],
        'this work':  [16.1344/0.2082, 90.5813/2.4599, 32.1934/1.0542, 12.6965/0.2042, 50.7354/2.4181],
        '[GAP]':  [16.1344/0.0081, 90.5813/0.05163, 32.1934/0.0209, 12.6965/0.00539, 50.7354/0.01478]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'baseline', 'this work', '[GAP]'])
label=('baseline', 'this work', '[GAP]')
# Setting the positions and width for the bars
pos = list(range(len(df['baseline'])))
width = 0.15
ecolor='k'
lw=0.5
print pos

#cmap = plt.get_cmap('jet')
#colors = cmap(np.linspace(0, 1.0, len(fuck_label)))

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['baseline'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        hatch=4*'/',
        # with alpha 0.5
        alpha=0.5,
        # with color
        #color=colors[0],
        color='w',
        # with label the first value in first_name
        label=label[0])

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['this work'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
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
        df['[GAP]'],
        # of width
        width,
        linewidth=lw,
        edgecolor='k',
        # with alpha 0.5
        alpha=0.5,
        # with color
        hatch=4*'-',
        color='w',
        #color=colors[2],
        # with label the third value in first_name
        label=label[2])


# Set the y axis label
ax.set_ylabel('Normalized Performance')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 1 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5'] + df['c6'] + df['c7'] + df['c8'] + df['c9'])] )

# Adding the legend and showing the plot
plt.legend(['baseline', 'this work', '[GAP]'], loc='upper left')
ax.grid(linewidth='0.5')
ax.xaxis.grid(False)
#plt.show()

plt.savefig("../overall-performance.pdf", bbox_inches='tight')
