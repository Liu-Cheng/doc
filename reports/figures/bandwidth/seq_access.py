#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

bandwidth=(8662.4, 8527.6, 8493.7, 8379.1, 7936.5, 6644.5, 4065.4, 1146.7, 269.3)
dataset=('256MB', '128MB', '32MB', '8MB', '2MB', '512KB', '128KB', '32KB', '8KB');
xdata=np.arange(len(dataset));
ax.plot(xdata, bandwidth, 'o-')
ax.set_xticks(xdata);
ax.set_xticklabels(dataset)
ax.set_xlabel('Data Size (MB)')
ax.set_ylabel('Bandwidth (MB/s)')
# ax.set_title('memory bandwidth with sequential access')
ax.grid(True)
plt.show()

fig.set_size_inches(8, 6)
fig.savefig("../seq_access.pdf", bbox_inches='tight')


