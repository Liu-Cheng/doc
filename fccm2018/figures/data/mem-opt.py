#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'graph': ['Youtube', 'LiveJournal', 'Pokec', 'RMAT-19-32', 'RMAT-21-32'],
        'cache': [16.1344/16.1344, 90.5813/90.5813, 32.1934/32.1934, 12.6965/12.6965, 50.7354/50.7354],
        'hash': [16.1344/5.5074, 90.5813/48.601, 32.1934/20.7189, 12.6965/10.7273, 50.7354/42.7774],
        'hub-buffer': [16.1344/5.2948, 90.5813/47.7471, 32.1934/20.4841, 12.6965/10.6896, 50.7354/42.607],
        '': [16.1344/4.7289, 90.5813/45.5692, 32.1934/19.747, 12.6965/10.519, 50.7354/41.9917],
        'c5': [16.1344/3.888, 90.5813/40.9439, 32.1934/17.9292, 12.6965/9.7478, 50.7354/38.9701],
        'c6': [16.1344/1.4022, 90.5813/9.7264, 32.1934/3.8728, 12.6965/2.1245, 50.7354/8.6928],
        'c7': [16.1344/1.4053, 90.5813/9.7447, 32.1934/3.9781, 12.6965/2.1248, 50.7354/8.7066],
        'c8': [16.1344/11.203, 90.5813/116.173, 32.1934/50.658, 12.6965/27.400, 50.7354/109.523],
        'c9': [16.1344/5.4649, 90.5813/51.455, 32.1934/22.1605, 12.6965/11.5924, 50.7354/46.5335]
        }
df = pd.DataFrame(raw_data, columns = ['graph', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'])
fuck_label=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9')
# Setting the positions and width for the bars
pos = list(range(len(df['c1'])))
width = 0.1
print pos

cmap = plt.get_cmap('jet')
colors = cmap(np.linspace(0, 1.0, len(fuck_label)))

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['c1'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[0],
        # with label the first value in first_name
        label=fuck_label[0])

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
        color=colors[1],
        # with label the second value in first_name
        label=fuck_label[1])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['post_score'] data,
        df['c3'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[2],
        # with label the third value in first_name
        label=fuck_label[2])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        #using df['post_score'] data,
        df['c4'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[3],
        # with label the third value in first_name
        label=fuck_label[3])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],
        #using df['post_score'] data,
        df['c5'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[4],
        # with label the third value in first_name
        label=fuck_label[4])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos],
        #using df['post_score'] data,
        df['c6'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[5],
        # with label the third value in first_name
        label=fuck_label[5])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*6 for p in pos],
        #using df['post_score'] data,
        df['c7'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[6],
        # with label the third value in first_name
        label=fuck_label[6])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*7 for p in pos],
        #using df['post_score'] data,
        df['c8'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[7],
        # with label the third value in first_name
        label=fuck_label[7])


# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*8 for p in pos],
        #using df['post_score'] data,
        df['c9'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color=colors[8],
        # with label the third value in first_name
        label=fuck_label[8])

# Set the y axis label
ax.set_ylabel('Performance Speedup')

# Set the chart's title
#ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 4.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['graph'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5'] + df['c6'] + df['c7'] + df['c8'] + df['c9'])] )

# Adding the legend and showing the plot
plt.legend(['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'], loc='upper left')
plt.grid()
#plt.show()

plt.savefig("../pipeline-performance.pdf", bbox_inches='tight')
