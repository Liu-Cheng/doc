#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('./burst_len_youtube.txt')
#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

ax = plt.subplot(111)
burst_len = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217,
        218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315,
        316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415,
        416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 427, 428, 429, 430, 431, 432, 433, 434, 435, 437, 438, 439, 440, 441, 442, 443, 445, 446, 447, 448, 449, 450, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 480, 483, 484, 485, 486, 488, 489, 490, 491, 492, 493, 494, 495, 497, 499, 500, 501, 502, 503, 504, 505, 506, 508, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526,
        528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 560, 563, 567, 568, 569, 571, 572, 573, 574, 575, 576, 577, 579, 581, 582, 583, 584, 585, 586, 588, 591, 592, 595, 596, 597, 598, 601, 602, 603, 604, 605, 607, 609, 610, 611, 612, 614, 615, 617, 618, 620, 624, 625, 626, 627, 628, 629, 632, 633, 634, 636, 640, 643, 644, 646, 648, 649, 650, 651, 652, 654, 656, 657, 658, 659, 660, 661, 662,
        663, 667, 668, 671, 672, 673, 674, 676, 678, 680, 681, 682, 684, 685, 686, 688, 689, 690, 692, 697, 699, 702, 704, 705, 706, 707, 709, 710, 713, 715, 716, 717, 718, 719, 720, 721, 725, 726, 729, 730, 731, 732, 736, 737, 739, 741, 743, 744, 747, 748, 749, 751, 753, 754, 755, 756, 760, 761, 763, 764, 765, 766, 768, 771, 772, 776, 778, 781, 784, 785, 788, 790, 793, 794, 795, 803, 804, 808, 812, 814, 815, 817, 819, 820, 821, 824, 825, 833, 834, 836, 838, 839, 841, 844, 845, 847, 848, 850,
        852, 853, 854, 855, 856, 858, 860, 862, 864, 866, 869, 870, 871, 872, 873, 874, 877, 882, 883, 887, 889, 892, 894, 897, 899, 916, 918, 922, 924, 925, 926, 928, 932, 933, 947, 948, 953, 957, 964, 967, 969, 971, 972, 973, 980, 981, 987, 988, 990, 996, 1000, 1003, 1004, 1007, 1008, 1012, 1013, 1015, 1018, 1019, 1020, 1022, 1023, 1024, 1033, 1037, 1040, 1043, 1045, 1046, 1058, 1059, 1060, 1061, 1064, 1079, 1085, 1086, 1089, 1095, 1097, 1098, 1101, 1103, 1104, 1107, 1108, 1113, 1116, 1130,
        1131, 1132, 1144, 1145, 1150, 1152, 1157, 1158, 1161, 1163, 1172, 1174, 1178, 1183, 1198, 1208, 1212, 1229, 1230, 1239, 1244, 1246, 1251, 1254, 1258, 1276, 1278, 1282, 1283, 1287, 1288, 1297, 1310, 1315, 1321, 1333, 1337, 1341, 1350, 1365, 1369, 1379, 1392, 1406, 1407, 1416, 1419, 1421, 1427, 1436, 1442, 1455, 1459, 1478, 1480, 1481, 1486, 1491, 1495, 1511, 1532, 1533, 1558, 1565, 1571, 1582, 1583, 1586, 1588, 1589, 1594, 1622, 1630, 1648, 1651, 1666, 1707, 1718, 1729, 1730, 1761, 1762,
        1771, 1808, 1815, 1816, 1823, 1841, 1853, 1860, 1869, 1883, 1884, 1898, 1903, 1924, 1945, 1951, 1959, 1965, 1971, 1992, 2015, 2020, 2058, 2067, 2077, 2083, 2088, 2094, 2100, 2113, 2126, 2128, 2135, 2161, 2164, 2188, 2197, 2199, 2202, 2204, 2211, 2217, 2252, 2257, 2263, 2325, 2334, 2355, 2374, 2378, 2380, 2400, 2444, 2464, 2488, 2504, 2535, 2591, 2628, 2634, 2720, 2742, 2753, 2763, 2799, 2800, 2818, 2830, 2837, 2866, 2924, 2956, 2992, 3024, 3035, 3100, 3114, 3160, 3394, 3506, 3621, 3707,
        4044, 4217, 4253, 4352, 4364, 4422, 4877, 4899, 5393, 6102, 7917, 8843, 9762, 10461, 11281, 14641, 28754)
burst_freq = (7712676, 182237, 92860, 55876, 36733, 26149, 19340, 15372, 12020, 9600, 7889, 6625, 5513, 4790, 4175, 3554, 3147, 2746, 2502, 2285, 2076, 1887, 1700, 1555, 1507, 1291, 1256, 1077, 1072, 954, 891, 818, 823, 756, 737, 640, 640, 535, 583, 472, 535, 473, 449, 431, 379, 396, 377, 364, 328, 321, 342, 287, 282, 266, 244, 270, 293, 250, 243, 232, 257, 222, 190, 200, 203, 188, 163, 168, 154, 168, 152, 152, 161, 142, 141, 124, 124, 120, 148, 121, 117, 125, 124, 103, 93, 103, 93, 102, 80, 84,
        66, 109, 77, 103, 74, 85, 78, 86, 85, 103, 84, 60, 69, 72, 71, 64, 57, 60, 60, 56, 53, 50, 42, 53, 55, 56, 54, 67, 43, 58, 42, 40, 39, 60, 36, 35, 30, 35, 48, 43, 42, 38, 31, 38, 38, 32, 23, 33, 33, 31, 42, 34, 30, 36, 44, 37, 27, 31, 33, 31, 30, 28, 23, 27, 24, 24, 18, 25, 31, 30, 23, 29, 21, 25, 21, 26, 25, 25, 29, 20, 26, 30, 15, 14, 19, 31, 31, 19, 20, 17, 20, 19, 22, 23, 13, 21, 21, 19, 20, 21, 16, 15, 19, 22, 13, 20, 20, 12, 13, 13, 11, 19, 17, 11, 12, 13, 21, 18, 17, 9, 21, 16,
        12, 11, 14, 12, 13, 17, 11, 20, 20, 16, 16, 13, 12, 10, 7, 13, 10, 19, 10, 17, 6, 8, 12, 7, 11, 11, 11, 10, 15, 9, 13, 6, 8, 10, 13, 5, 4, 9, 13, 11, 3, 11, 5, 11, 15, 15, 9, 4, 12, 5, 15, 14, 10, 12, 10, 11, 4, 12, 10, 6, 10, 9, 8, 13, 6, 4, 12, 7, 5, 7, 6, 4, 8, 7, 6, 4, 3, 11, 6, 10, 6, 6, 9, 9, 10, 11, 11, 5, 4, 5, 5, 2, 6, 6, 9, 4, 7, 6, 8, 9, 6, 7, 3, 9, 2, 7, 6, 9, 5, 2, 3, 6, 3, 3, 8, 4, 3, 5, 2, 8, 5, 4, 6, 4, 7, 4, 4, 7, 4, 4, 6, 5, 2, 7, 2, 2, 5, 4, 7, 7, 1, 5, 4, 2, 3, 3, 6,
        4, 5, 2, 2, 3, 4, 2, 5, 5, 2, 6, 4, 4, 5, 5, 4, 3, 3, 4, 3, 6, 2, 3, 3, 3, 1, 2, 5, 1, 5, 1, 3, 5, 1, 3, 4, 1, 2, 4, 2, 3, 9, 1, 5, 2, 3, 2, 2, 1, 3, 3, 2, 4, 1, 2, 2, 3, 2, 5, 2, 1, 3, 4, 2, 4, 3, 2, 2, 6, 3, 3, 4, 2, 2, 5, 2, 2, 4, 3, 4, 3, 5, 3, 4, 3, 3, 1, 5, 1, 3, 2, 2, 2, 1, 3, 2, 6, 6, 1, 3, 4, 5, 1, 2, 2, 4, 4, 3, 1, 3, 2, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 1, 4, 3, 2, 4, 6, 4, 1, 4, 2, 1, 2, 3, 1, 2, 1, 1, 3, 3, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 3, 2, 3, 1,
        2, 1, 2, 1, 2, 3, 1, 1, 2, 3, 1, 5, 3, 1, 1, 1, 2, 1, 1, 4, 1, 2, 3, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 3, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 3, 1, 1, 3, 1,
        1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

transfer_amount=( 9520293, 1457896, 1114320, 894016, 734660, 627576, 541520, 491904, 432720, 384000, 347116, 318000, 286676, 268240, 250500, 227456, 213996, 197712, 190152, 182800, 174384, 166056, 156400, 149280, 150700, 134264, 135648, 120624, 124352, 114480, 110484, 104704, 108636, 102816, 103180, 92160, 94720, 81320, 90948, 75520, 87740, 79464, 77228, 75856, 68220, 72864, 70876, 69888, 64288, 64200, 69768, 59696, 59784, 57456, 53680, 60480, 66804, 58000, 57348, 55680, 62708, 55056, 47880,
        51200, 52780, 49632, 43684, 45696, 42504, 47040, 43168, 43776, 47012, 42032, 42300, 37696, 38192, 37440, 46768, 38720, 37908, 41000, 41168, 34608, 31620, 35432, 32364, 35904, 28480, 30240, 24024, 40112, 28644, 38728, 28120, 32640, 30264, 33712, 33660, 41200, 33936, 24480, 28428, 29952, 29820, 27136, 24396, 25920, 26160, 24640, 23532, 22400, 18984, 24168, 25300, 25984, 25272, 31624, 20468, 27840, 20328, 19520, 19188, 29760, 18000, 17640, 15240, 17920, 24768, 22360, 22008, 20064, 16492,
        20368, 20520, 17408, 12604, 18216, 18348, 17360, 23688, 19312, 17160, 20736, 25520, 21608, 15876, 18352, 19668, 18600, 18120, 17024, 14076, 16632, 14880, 14976, 11304, 15800, 19716, 19200, 14812, 18792, 13692, 16400, 13860, 17264, 16700, 16800, 19604, 13600, 17784, 20640, 10380, 9744, 13300, 21824, 21948, 13528, 14320, 12240, 14480, 13832, 16104, 16928, 9620, 15624, 15708, 14288, 15120, 15960, 12224, 11520, 14668, 17072, 10140, 15680, 15760, 9504, 10348, 10400, 8844, 15352, 13804, 8976,
        9840, 10712, 17388, 14976, 14212, 7560, 17724, 13568, 10224, 9416, 12040, 10368, 11284, 14824, 9636, 17600, 17680, 14208, 14272, 11648, 10800, 9040, 6356, 11856, 9160, 17480, 9240, 15776, 5592, 7488, 11280, 6608, 10428, 10472, 10516, 9600, 14460, 8712, 12636, 5856, 7840, 9840, 12844, 4960, 3984, 9000, 13052, 11088, 3036, 11176, 5100, 11264, 15420, 15480, 9324, 4160, 12528, 5240, 15780, 14784, 10600, 12768, 10680, 11792, 4304, 12960, 10840, 6528, 10920, 9864, 8800, 14352, 6648, 4448,
        13392, 7840, 5620, 7896, 6792, 4544, 9120, 8008, 6888, 4608, 3468, 12760, 6984, 11680, 7032, 7056, 10620, 10656, 11880, 13112, 13156, 6000, 4816, 6040, 6060, 2432, 7320, 7344, 11052, 4928, 8652, 7440, 9952, 11232, 7512, 8792, 3780, 11376, 2536, 8904, 7656, 11520, 6420, 2576, 3876, 7776, 3900, 3912, 10464, 5248, 3948, 6600, 2648, 10624, 6660, 5344, 8040, 5376, 9436, 5408, 5424, 9520, 5456, 5472, 8256, 6900, 2768, 9716, 2784, 2792, 7000, 5616, 9856, 9884, 1416, 7100, 5696, 2856, 4296,
        4308, 8640, 5776, 7240, 2904, 2912, 4380, 5856, 2936, 7360, 7380, 2960, 8904, 5952, 5968, 7480, 7500, 6016, 4524, 4536, 6064, 4560, 9144, 3056, 4596, 4608, 4620, 1544, 3096, 7760, 1556, 7800, 1564, 4704, 7860, 1576, 4740, 6336, 1592, 3192, 6400, 3208, 4824, 14508, 1616, 8100, 3248, 4884, 3264, 3272, 1640, 4932, 4944, 3304, 6624, 1660, 3328, 3336, 5016, 3352, 8400, 3368, 1688, 5076, 6784, 3400, 6832, 5136, 3432, 3440, 10344, 5184, 5196, 6944, 3480, 3496, 8760, 3512, 3520, 7056, 5304,
        7088, 5340, 8920, 5364, 7168, 5388, 5400, 1808, 9060, 1816, 5460, 3648, 3656, 3664, 1836, 5520, 3688, 11088, 11112, 1856, 5580, 7456, 9360, 1876, 3760, 3768, 7552, 7568, 5688, 1900, 5712, 3816, 3824, 3840, 3864, 3872, 3880, 5832, 1952, 3912, 3920, 3928, 3936, 1972, 7904, 5940, 3976, 7984, 12000, 8016, 2008, 8048, 4032, 2020, 4048, 6096, 2040, 4088, 2048, 2052, 6168, 6180, 4128, 4136, 2072, 2076, 4160, 2084, 4176, 2092, 4192, 4200, 4208, 2112, 2116, 4240, 4248, 2128, 2132, 2136, 2140,
        6432, 4296, 6456, 2156, 4320, 2164, 4336, 2172, 4360, 6552, 2188, 2192, 4392, 6600, 2204, 11040, 6636, 2216, 2220, 2224, 4456, 2232, 2240, 9008, 2268, 4544, 6828, 4568, 2288, 4584, 2296, 2300, 2304, 4616, 2316, 2324, 4656, 2332, 4672, 2340, 2344, 4704, 2364, 2368, 2380, 4768, 4776, 4784, 4808, 7224, 2412, 2416, 2420, 2428, 2436, 2440, 2444, 2448, 9824, 2460, 2468, 7416, 4960, 2496, 2500, 5008, 2508, 2512, 5032, 2528, 5064, 5072, 2544, 2560, 7716, 5152, 5168, 2592, 2596, 2600, 2604, 2608,
        2616, 2624, 2628, 2632, 5272, 5280, 2644, 2648, 2652, 8004, 5344, 2684, 5376, 2692, 2696, 2704, 2712, 2720, 2724, 2728, 5472, 8220, 2744, 2752, 8268, 2760, 2768, 2788, 2796, 2808, 2816, 5640, 2824, 5656, 2836, 5680, 2852, 2860, 8592, 2868, 2872, 2876, 2880, 5768, 8700, 2904, 2916, 5840, 2924, 5856, 2944, 2948, 2956, 2964, 2972, 2976, 2988, 8976, 5992, 9012, 3012, 6032, 9060, 3024, 3040, 3044, 3052, 3056, 3060, 3064, 3072, 3084, 3088, 3104, 3112, 6248, 6272, 3140, 3152, 3160, 3172, 9528,
        3180, 3212, 9648, 3232, 3248, 3256, 3260, 6536, 3276, 3280, 6568, 3296, 3300, 3332, 3336, 3344, 3352, 3356, 3364, 3376, 3380, 3388, 3392, 3400, 3408, 3412, 3416, 3420, 6848, 3432, 3440, 3448, 3456, 3464, 3476, 3480, 6968, 3488, 3492, 3496, 3508, 3528, 3532, 3548, 3556, 3568, 3576, 3588, 3596, 3664, 3672, 3688, 3696, 3700, 3704, 7424, 3728, 3732, 3788, 3792, 7624, 3828, 3856, 3868, 3876, 3884, 7776, 7784, 3920, 3924, 3948, 3952, 3960, 3984, 8000, 4012, 4016, 4028, 8064, 8096, 8104, 4060,
        4072, 4076, 4080, 4088, 4092, 4096, 4132, 4148, 4160, 4172, 4180, 4184, 8464, 4236, 4240, 4244, 8512, 4316, 4340, 4344, 4356, 4380, 4388, 4392, 4404, 4412, 4416, 4428, 4432, 4452, 4464, 4520, 4524, 9056, 4576, 4580, 4600, 4608, 4628, 4632, 4644, 4652, 4688, 4696, 4712, 4732, 4792, 4832, 4848, 4916, 4920, 4956, 4976, 4984, 5004, 5016, 5032, 5104, 5112, 5128, 5132, 5148, 5152, 5188, 5240, 5260, 5284, 5332, 5348, 5364, 5400, 5460, 5476, 5516, 5568, 11248, 5628, 5664, 5676, 5684, 5708, 5744,
        5768, 5820, 5836, 5912, 5920, 5924, 11888, 5964, 5980, 6044, 6128, 6132, 6232, 6260, 6284, 6328, 6332, 6344, 6352, 6356, 6376, 6488, 6520, 6592, 6604, 6664, 6828, 6872, 20748, 6920, 7044, 7048, 7084, 7232, 14520, 7264, 7292, 7364, 7412, 7440, 7476, 7532, 7536, 7592, 7612, 7696, 7780, 7804, 7836, 7860, 7884, 7968, 8060, 8080, 8232, 8268, 8308, 8332, 8352, 8376, 8400, 8452, 8504, 8512, 8540, 8644, 8656, 8752, 8788, 8796, 8808, 8816, 8844, 8868, 9008, 9028, 9052, 9300, 9336, 9420, 9496,
        9512, 9520, 9600, 9776, 9856, 9952, 10016, 10140, 10364, 10512, 10536, 10880, 10968, 11012, 11052, 11196, 11200, 11272, 11320, 11348, 22928, 11696, 11824, 11968, 12096, 12140, 12400, 12456, 12640, 13576, 14024, 14484, 14828, 16176, 16868, 17012, 17408, 17456, 17688, 19508, 19596, 21572, 24408, 31668, 35372, 39048, 41844, 45124, 58564, 115016)
measure_burst=(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
        16384, 32768, 65536, 131072, 262144, 524288, 1048576)
measure_lat_1lane=(144.6,
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
measure_lat_2lane=(85.4227,
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
measure_lat_4lane=(87.2427,
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
index = 0
#estimated_lat = []
estimated_bandwidth_1lane = []
estimated_bandwidth_2lane = []
estimated_bandwidth_4lane = []
while(index < len(burst_len)):
    i = 0;
    while(burst_len[index] > measure_burst[i] and i < len(measure_burst) - 1):
        i = i + 1
    if(burst_len[index] == measure_burst[i]):
        lat_1lane = measure_lat_1lane[i]
        lat_2lane = measure_lat_2lane[i]
        lat_4lane = measure_lat_4lane[i];
    else:
        slope_1lane = (measure_lat_1lane[i-1] - measure_lat_1lane[i])/(measure_burst[i] - measure_burst[i-1])
        slope_2lane = (measure_lat_2lane[i-1] - measure_lat_2lane[i])/(measure_burst[i] - measure_burst[i-1])
        slope_4lane = (measure_lat_4lane[i-1] - measure_lat_4lane[i])/(measure_burst[i] - measure_burst[i-1])
        lat_1lane = measure_lat_1lane[i-1] - slope_1lane * (burst_len[index] - measure_burst[i-1])
        lat_2lane = measure_lat_2lane[i-1] - slope_2lane * (burst_len[index] - measure_burst[i-1])
        lat_4lane = measure_lat_4lane[i-1] - slope_4lane * (burst_len[index] - measure_burst[i-1])
    #lat = lat * transfer_amount[index]
    #estimated_lat.append(lat)
    estimated_bandwidth_1lane.append(1000.0/lat_1lane)
    estimated_bandwidth_2lane.append(1000.0/lat_2lane)
    estimated_bandwidth_4lane.append(1000.0/lat_4lane)
    index = index + 1

#total_access_time = sum(estimated_lat)
#accumulated_lat_percent=[]
#accumulated_lat = 0.0
#for lat in estimated_lat:
#    accumulated_lat += lat;
#    accumulated_lat_percent.append(accumulated_lat/total_access_time)

plt.loglog(burst_len, burst_freq, 'bo', label='Burst Distribution')
#plt.loglog(burst_len, transfer_amount, 'rs', label='Amount of Transfer')
#plt.semilogy(burst_len, burst_freq, 'bo')
ax.set_xlabel('Burst Length')
ax.set_ylabel('# of Bursts')

ay = ax.twinx()
ay.plot(burst_len, estimated_bandwidth_1lane, 'r^', label='Burst Bandwidth (1-lane)')
ay.plot(burst_len, estimated_bandwidth_2lane, 'gp', label='Burst Bandwidth (2-lane)')
ay.plot(burst_len, estimated_bandwidth_4lane, 'ys', label='Burst Bandwidth (4-lane)')
#ay.semilogy(burst_len, transfer_amount, 'ro')
ay.set_ylabel('Memory Bandwidth (MB/s)')

lx, labelx = ax.get_legend_handles_labels()
ly, labely = ay.get_legend_handles_labels()
ay.legend(lx + ly, labelx + labely, loc='upper center')

plt.grid(True)
plt.tight_layout()
#plt.show()
#fig.set_size_inches(8, 6)
plt.savefig("../burst_len_youtube.pdf", bbox_inches='tight', )

