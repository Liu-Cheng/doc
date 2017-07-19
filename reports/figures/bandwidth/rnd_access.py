#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

bandwidth=(26.95, 26.92, 26.96, 26.94, 26.95, 26.94, 26.84, 26.52, 25.324)
dataset=('256MB', '128MB', '32MB', '8MB', '2MB', '512KB', '128KB', '32KB', '8KB');
xdata=np.arange(len(dataset));
ax.plot(xdata, bandwidth, 'o-')
ax.set_xticks(xdata);
ax.set_xticklabels(dataset)
ax.set_xlabel('Data Size (MB)')
ax.set_ylabel('Bandwidth (MB/s)')
# ax.set_title('memory bandwidth with random access')
plt.grid(True)
plt.show()

fig.set_size_inches(8, 6)
fig.savefig("../rnd_access.pdf", bbox_inches='tight')


