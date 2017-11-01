#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)
burst_len=(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
        16384, 32768, 65536, 131072, 262144, 524288, 1048576)
xlabel=('1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096',
        '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576')

avg_lat_aligned_1_lane=(
        139.299,
        116.531,
        103.088,
        44.7441,
        23.4594,
        13.0615,
        7.82565,
        5.29667,
        3.93645,
        3.25469,
        2.99103,
        2.90821,
        2.86494,
        2.84156,
        2.83015,
        2.83548,
        2.82962,
        2.82417,
        2.8213,
        2.8204,
        2.81952)
avg_lat_aligned_2_lane=(83.403,
        79.4517,
        49.8661,
        21.1353,
        11.053,
        6.1206,
        3.78309,
        2.68819,
        2.80583,
        2.41133,
        2.83059,
        3.10294,
        3.21664,
        3.24875,
        3.27196,
        3.29181,
        3.28964,
        3.28445,
        3.28032,
        3.27842,
        3.27723)
avg_lat_aligned_4_lane=(
        87.2365,
        79.2914,
        39.4741,
        18.0921,
        7.84265,
        4.46393,
        3.00778,
        2.80309,
        3.51313,
        3.38905,
        3.277,
        3.23267,
        3.20955,
        3.19877,
        3.195,
        3.19347,
        3.19273,
        3.19326,
        3.19266,
        3.19239,
        3.19218)
avg_lat_unaligned_1_lane=(
        144.6,
        122.241,
        103.441,
        48.9835,
        26.6786,
        19.5113,
        16.2053,
        13.508,
        11.7516,
        10.2765,
        7.58283,
        5.05561,
        3.78905,
        3.23154,
        3.02393,
        2.94255,
        2.87799,
        2.84908,
        2.83384,
        2.82638,
        2.82265)
avg_lat_unaligned_2_lane=(
        85.4227,
        80.7041,
        57.8135,
        25.4667,
        15.8736,
        12.6045,
        9.11723,
        8.27869,
        7.81048,
        6.84269,
        5.22089,
        4.22288,
        4.02895,
        3.66041,
        3.46617,
        3.37151,
        3.31445,
        3.28053,
        3.26757,
        3.25973,
        3.25497)
avg_lat_unaligned_4_lane=(
        87.2427,
        82.4752,
        42.3055,
        22.9417,
        12.4717,
        10.2009,
        9.52618,
        9.21937,
        8.44548,
        7.79352,
        6.2176,
        5.01824,
        4.19152,
        3.72498,
        3.46138,
        3.33175,
        3.25859,
        3.23982,
        3.21685,
        3.21908,
        3.20436)

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

