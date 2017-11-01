#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#c1 S3(cache)
#c2 S3(cache) + S4(cache) + S5(cache)
#c3 S2(cache) + S3(cache) + S4(cache) + S5(cache)
#c4 S2(cache) + S3(cache) + S4-5(cache)
#c5 S2(cache) + S3(cache) + S4(cache) + S5(2way-cache)

raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        'c1':  [1.4022/0.622, 9.7264/4.9670, 3.8728/2.2921, 2.1245/0.7186, 8.6928/3.1482],
        'c2':  [1.4022/0.462, 9.7264/4.3352, 3.8728/1.5297, 2.1245/0.6692, 8.6928/3.6212],
        'c3':  [1.4022/0.464, 9.7264/4.3420, 3.8728/1.4992, 2.1245/0.6694, 8.6928/3.6276],
        'c4':  [1.4022/0.444, 9.7264/6.2370, 3.8728/1.7054, 2.1245/0.6595, 8.6928/6.0361]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'c1', 'c2', 'c3', 'c4'])
label=('c1', 'c2', 'c3', 'c4')
# Setting the positions and width for the bars
pos = list(range(len(df['c1'])))
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
        df['c1'],
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
        df['c2'],
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
        df['c3'],
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
        alpha=0.5,
        # with color
        #color=colors[3],
        hatch=4*'\\',
        color='w',
        # with label the third value in first_name
        label=label[3])


# Set the y axis label
ax.set_ylabel('Performance Speedup')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5'] + df['c6'] + df['c7'] + df['c8'] + df['c9'])] )

# Adding the legend and showing the plot
plt.legend(['cache(S4)', 'cache(S4, S5, S6)', 'cache(S3, S4, S5, S6)', 'cache(S3, S4, S5S6)'], ncol=2, loc='lower center')
ax.grid(linewidth='0.5')
ax.xaxis.grid(False)
#plt.show()

plt.savefig("../cache-performance.pdf", bbox_inches='tight')
