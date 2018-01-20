#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

# vector size = 64*1024*1024
# burst_len = 1
# stride = 4, 8, 16, 32, 64, 128, 256, 512, 1024
avg_lat_64M = ()
avg_lat_32M = ()
avg_lat_16M = ()
avg_lat_4M = ()
avg_lat_1M = ()
avg_lat_512K = ()
avg_lat_256K = ()
avg_lat_128K = ()
avg_lat_64K = ()

xdata=np.arange(len(burst_len))
plt.plot(xdata, avg_lat_unaligned_1_lane, 'bp-', label='Latency (1 lane)')
plt.plot(xdata, avg_lat_unaligned_2_lane, 'bs-', label='Latency (2 parallel lanes)')
plt.plot(xdata, avg_lat_unaligned_4_lane, 'b^-', label='Latency (4 parallel lanes)')
plt.plot(xdata, avg_lat_aligned_1_lane, 'kp-', label='Latency (1 lane)')
plt.plot(xdata, avg_lat_aligned_2_lane, 'ks-', label='Latency (2 parallel lanes)')
plt.plot(xdata, avg_lat_aligned_4_lane, 'k^-', label='Latency (4 parallel lanes)')


ax.set_xticks(xdata);
ax.set_xticklabels(xlabel)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
ax.set_xlabel('Burst Length')
ax.set_ylabel('Average Latency per Word (ns)')

ay = ax.twinx()
bandwidth_aligned_1_lane=(27.3849,
        32.7355,
        37.0042,
        85.2559,
        162.609,
        292.057,
        487.461,
        720.207,
        969.069,
        1172.06,
        1275.38,
        1311.7,
        1331.51,
        1342.46,
        1347.88,
        1345.35,
        1348.13,
        1350.73,
        1352.1,
        1352.04,
        1352.96)
bandwidth_aligned_2_lane=(
        45.7923,
        48.0128,
        76.4989,
        180.489,
        345.126,
        623.255,
        1008.35,
        1419.06,
        1359.56,
        1581.99,
        1347.67,
        1229.38,
        1185.93,
        1174.21,
        1165.88,
        1158.85,
        1159.61,
        1161.44,
        1162.91,
        1163.58,
        1164)
bandwidth_aligned_4_lane=(
        43.7282,
        48.1098,
        96.638,
        210.849,
        486.404,
        854.56,
        1268.28,
        1360.89,
        1085.84,
        1125.6,
        1164.08,
        1180.05,
        1188.55,
        1192.55,
        1193.96,
        1194.53,
        1194.81,
        1194.61,
        1194.83,
        1194.94,
        1195.01)

bandwidth_unaligned_1_lane=(
        26.381,
        31.2063,
        36.8782,
        77.8772,
        142.987,
        195.512,
        235.398,
        282.402,
        324.611,
        371.208,
        503.07,
        754.547,
        1006.77,
        1180.46,
        1261.5,
        1296.39,
        1325.47,
        1338.92,
        1346.12,
        1349.68,
        1351.46)
bandwidth_unaligned_2_lane = (
        44.6567,
        47.2677,
        65.9828,
        149.792,
        240.317,
        302.646,
        418.405,
        460.785,
        488.407,
        557.485,
        730.661,
        903.341,
        946.822,
        1042.15,
        1100.55,
        1131.45,
        1150.93,
        1162.83,
        1167.44,
        1170.25,
        1171.96)
bandwidth_unaligned_4_lane=(
        43.7251,
        46.2527,
        90.1702,
        166.278,
        305.867,
        373.957,
        400.444,
        413.77,
        451.685,
        489.47,
        613.532,
        760.167,
        910.098,
        1024.08,
        1102.07,
        1144.95,
        1170.66,
        1177.44,
        1185.85,
        1185.03,
        1190.47)

ay.plot(xdata, bandwidth_unaligned_1_lane, 'rp-', label='bandwidth (1 lane)')
ay.plot(xdata, bandwidth_unaligned_2_lane, 'rs-', label='bandwidth (2 parallel lanes)')
ay.plot(xdata, bandwidth_unaligned_4_lane, 'r^-', label='bandwidth (4 parallel lanes)')
ay.plot(xdata, bandwidth_aligned_1_lane, 'yp-', label='bandwidth (1 lane)')
ay.plot(xdata, bandwidth_aligned_2_lane, 'ys-', label='bandwidth (2 parallel lanes)')
ay.plot(xdata, bandwidth_aligned_4_lane, 'y^-', label='bandwidth (4 parallel lanes)')

ay.set_ylabel('bandwidth (MB/s)')

#lx, labelx = ax.get_legend_handles_labels()
#ly, labely = ay.get_legend_handles_labels()
#ay.legend(lx + ly, labelx + labely, loc='right')

plt.tight_layout()
plt.grid(True)
#plt.show()
#fig.set_size_inches(8, 6)
plt.savefig("../mem_latency.pdf", bbox_inches='tight', )

