#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.style.use('default')
#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize


ax = plt.subplot(111)
#live journal
#youtube

ngb=(1, 55, 44993, 1541217, 3077978, 1003505, 231769, 56553, 14187, 3636, 1013, 228, 63, 39, 11)
ngb_remove_repeat_vertex = (1, 55, 33915, 421223, 739176, 390580, 141779, 35801, 8451, 2166, 536, 126, 45, 22, 3)
ngb_remove_frontier_vertex = (1, 55, 33891, 390685, 524356, 307317, 129643, 33527, 7994, 2053, 503, 115, 45, 20, 3)
bfs_level=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15')
# resource_bram={}
# resource_ff={}
# resource_lut={}
# resource_dsp={}
xdata=np.arange(len(bfs_level))
x0 = [None] * len(bfs_level) # visited memory access
x1 = [None] * len(bfs_level) # redundant memory access
x2 = [None] * len(bfs_level) # valid memory access
for i in range(0, len(bfs_level)):
    x2[i] = ngb_remove_frontier_vertex[i]
    x1[i] = ngb[i] - ngb_remove_repeat_vertex[i]
    x0[i] = ngb_remove_repeat_vertex[i] - ngb_remove_frontier_vertex[i]

b2 = plt.bar(xdata, x2, width=0.4, color='C0')
b1 = plt.bar(xdata, x1, width=0.4, color='C1', bottom=x2)
b0 = plt.bar(xdata, x0, width=0.4, color='C2', bottom=np.array(x1) + np.array(x2))
plt.xticks(xdata);
#plt.xticklabels(bfs_level)
#for tick in ax.get_xticklabels():
#    tick.set_rotation(45)

plt.ylabel('Frontier Neighbor Distribution')
plt.xlabel('BFS Iterations')
# ax.set_title('memory bandwidth with random access')
ax.yaxis.grid(which='major')
#plt.grid(True)
#plt.show()
#ymin, ymax = ax.get_ylim();

#ay = ax.twinx()
#frontier_size=(1, 1, 54, 33890, 390632, 495648, 158941, 41349, 10692, 2665, 774, 171, 35, 26, 11 )
#ay.plot(xdata, frontier_size, 'go-', label='Frontier Size')
#ay.semilogy(burst_len, transfer_amount, 'ro')
#ay.set_ylabel('Frontier Size')
#ay.set_ylim(ymin, ymax)

#lx, labelx = ax.get_legend_handles_labels()
#ly, labely = ay.get_legend_handles_labels()
#ay.legend(lx + ly, labelx + labely, loc='right')

plt.legend([b0, b1, b2],
        ['Visited Vertices', 'Redundant Vertices', 'Valid Vertices'],
        fontsize=12,
        loc='best')

#plt.set_size_inches(8, 6)
plt.savefig("../neighbor_vertex.pdf", bbox_inches='tight')

