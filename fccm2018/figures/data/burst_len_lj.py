#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('./burst_len_youtube.txt')

ax = plt.subplot(111)
burst_len = (
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 759, 761, 763, 764, 765, 767, 768, 769, 770, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 790, 791, 793, 794, 798, 799, 800, 801, 803, 804, 806, 807, 808, 810, 812, 813, 814, 816, 820, 821, 824, 825, 826, 827, 829, 830, 833, 838, 844, 847, 853, 855, 857, 864, 871, 872, 873, 874, 875, 878, 879, 880, 883, 884, 885, 889, 890, 893, 897, 899, 900, 903, 904, 906, 910, 919, 924, 926, 929, 941, 943, 953, 956, 958, 959, 960, 962, 963, 966, 968, 969, 971, 974, 975, 976, 980, 982, 984, 985, 986, 987, 988, 989, 993, 994, 995, 996, 998, 999, 1005, 1007, 1012, 1030, 1050, 1052, 1067, 1075, 1086, 1098, 1104, 1116, 1126, 1134, 1143, 1146, 1173, 1205, 1215, 1225, 1228, 1230, 1242, 1253, 1266, 1288, 1344, 1358, 1369, 1371, 1411, 1467, 1498, 1517, 1556, 1557, 1569, 1577, 1588, 1796, 1827, 1851, 1858, 1976, 1997, 2321, 2376, 2497, 2584, 2829, 2894, 3265, 4572, 4758, 4879, 5597, 8180, 8428, 13050, 15163, 20293)
burst_freq = (73207237, 414612, 299593, 235346, 193632, 160403, 137371, 119365, 105763, 94033, 85603, 77562, 70666, 64979, 59556, 55132, 51907, 48104, 44930, 42070, 38867, 36542, 34184, 32452, 30601, 28615, 27283, 26068, 24337, 23006, 22007, 20829, 19602, 18776, 17764, 17077, 16337, 15483, 14791, 14124, 13590, 12849, 11929, 11556, 11274, 10700, 10349, 9963, 9410, 9279, 8797, 8537, 8103, 7792, 7491, 6945, 6816, 6683, 6456, 6157, 5791, 5635, 5533, 5401, 5027, 4892, 4901, 4582, 4378, 4219, 4094, 3934, 3877, 3706, 3588, 3645, 3467, 3248, 3169, 3076, 3028, 2929, 2915, 2631, 2685, 2509, 2497, 2396, 2432, 2333, 2345, 2112, 2099, 2033, 1925, 1880, 1919, 1809, 1740, 1785, 1699, 1627, 1574, 1504, 1477, 1404, 1434, 1339, 1352, 1306, 1324, 1294, 1217, 1316, 1107, 1191, 1130, 1143, 991, 1035, 1028, 963, 952, 955, 936, 911, 924, 874, 866, 846, 830, 749, 771, 810, 756, 747, 710, 746, 678, 678, 655, 622, 625, 628, 607, 616, 641, 551, 543, 554, 541, 512, 545, 549, 526, 454, 502, 454, 502, 518, 494, 482, 480, 456, 427, 419, 385, 402, 401, 394, 409, 400, 375, 407, 393, 357, 327, 351, 343, 356, 333, 342, 320, 326, 307, 340, 285, 321, 307, 310, 307, 278, 312, 301, 262, 258, 267, 281, 260, 271, 257, 246, 235, 241, 244, 284, 264, 236, 248, 233, 246, 218, 223, 203, 214, 236, 217, 260, 189, 191, 166, 176, 186, 186, 198, 171, 173, 164, 177, 176, 180, 162, 180, 164, 165, 156, 161, 140, 137, 162, 153, 173, 143, 164, 138, 135, 139, 129, 128, 134, 111, 133, 128, 127, 104, 107, 101, 119, 94, 117, 106, 103, 106, 92, 115, 115, 85, 93, 74, 166, 97, 90, 95, 87, 72, 78, 102, 96, 94, 82, 251, 97, 90, 80, 94, 93, 103, 113, 95, 82, 94, 78, 83, 88, 115, 133, 76, 82, 84, 65, 56, 78, 73, 77, 79, 80, 95, 136, 95, 83, 68, 91, 72, 78, 63, 48, 69, 52, 66, 59, 71, 50, 52, 56, 59, 54, 47, 59, 58, 49, 62, 69, 52, 61, 53, 41, 44, 43, 64, 43, 56, 62, 49, 39, 40, 50, 56, 52, 56, 39, 45, 46, 57, 50, 55, 53, 41, 36, 48, 36, 47, 38, 27, 39, 48, 38, 44, 40, 55, 47, 52, 36, 37, 39, 39, 37, 33, 35, 37, 36, 32, 36, 29, 29, 26, 39, 25, 46, 34, 22, 32, 37, 26, 41, 43, 21, 46, 33, 38, 30, 27, 18, 29, 31, 27, 21, 30, 16, 22, 33, 22, 27, 14, 27, 24, 27, 26, 27, 27, 20, 40, 25, 33, 28, 20, 21, 26, 23, 22, 16, 24, 22, 22, 18, 21, 23, 18, 23, 20, 29, 30, 12, 16, 21, 24, 19, 18, 14, 24, 22, 22, 24, 27, 25, 22, 33, 17, 23, 23, 27, 19, 29, 26, 26, 26, 15, 23, 19, 16, 23, 21, 29, 21, 23, 17, 27, 9, 24, 22, 21, 10, 26, 16, 22, 16, 10, 10, 18, 23, 14, 19, 17, 23, 17, 18, 14, 7, 16, 12, 14, 13, 15, 13, 12, 8, 13, 14, 13, 9, 13, 13, 10, 11, 10, 15, 8, 17, 14, 12, 11, 8, 13, 8, 12, 11, 17, 14, 8, 19, 19, 17, 19, 18, 9, 13, 13, 10, 5, 10, 16, 10, 10, 13, 9, 5, 10, 16, 9, 6, 14, 9, 14, 5, 8, 15, 10, 8, 16, 10, 7, 12, 6, 9, 11, 13, 8, 5, 9, 13, 8, 12, 4, 10, 15, 10, 11, 13, 10, 7, 3, 8, 9, 11, 9, 7, 12, 13, 7, 5, 10, 8, 14, 4, 8, 13, 4, 5, 8, 5, 8, 8, 7, 9, 14, 5, 8, 5, 9, 11, 8, 11, 6, 7, 12, 8, 10, 7, 8, 14, 12, 3, 8, 6, 5, 13, 2, 14, 8, 9, 11, 12, 13, 6, 5, 9, 8, 4, 11, 8, 12, 8, 12, 5, 12, 10, 18, 10, 10, 9, 7, 12, 6, 18, 6, 14, 6, 9, 12, 5, 12, 13, 12, 13, 7, 7, 12, 12, 13, 11, 11, 11, 5, 9, 13, 10, 12, 9, 9, 11, 9, 9, 6, 6, 8, 16, 12, 16, 9, 7, 13, 9, 13, 13, 5, 9, 13, 10, 8, 19, 8, 5, 10, 10, 14, 12, 5, 10, 12, 10, 11, 10, 11, 5, 9, 14, 12, 11, 12, 11, 4, 12, 6, 15, 6, 9, 8, 18, 13, 4, 12, 4, 4, 2, 7, 8, 7, 8, 6, 7, 10, 9, 13, 10, 7, 6, 2, 6, 2, 3, 5, 2, 1, 2, 3, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 2, 3, 1, 3, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

transfer_amount=( 75100597, 3316896, 3595116, 3765536, 3872640, 3849672, 3846388, 3819680, 3807468, 3761320, 3766532, 3722976, 3674632, 3638824, 3573360, 3528448, 3529676, 3463488, 3414680, 3365600, 3264828, 3215696, 3144928, 3115392, 3060100, 2975960, 2946564, 2919616, 2823092, 2760720, 2728868, 2666112, 2587464, 2553536, 2486960, 2459088, 2417876, 2353416, 2307396, 2259840, 2228760, 2158632, 2051788, 2033856, 2029320, 1968800, 1945612, 1912896, 1844360, 1855800, 1794588, 1775696, 1717836, 1683072, 1648020, 1555680, 1554048, 1550456, 1523616, 1477680, 1413004, 1397480, 1394316, 1382656, 1307020, 1291488, 1313468, 1246304, 1208328, 1181320, 1162696, 1132992, 1132084, 1096976, 1076400, 1108080, 1067836, 1013376, 1001404, 984320, 981072, 960712, 967780, 884016, 912900, 863096, 868956, 843392, 865792, 839880, 853580, 777216, 780828, 764408, 731500, 721920, 744572, 709128, 689040, 714000, 686396, 663816, 648488, 625664, 620340, 595296, 613752, 578448, 589472, 574640, 587856, 579712, 550084, 600096, 509220, 552624, 528840, 539496, 471716, 496800, 497552, 469944, 468384, 473680, 468000, 459144, 469392, 447488, 446856, 439920, 434920, 395472, 410172, 434160, 408240, 406368, 389080, 411792, 376968, 379680, 369420, 353296, 357500, 361728, 352060, 359744, 376908, 326192, 323628, 332400, 326764, 311296, 333540, 338184, 326120, 283296, 315256, 286928, 319272, 331520, 318136, 312336, 312960, 299136, 281820, 278216, 257180, 270144, 271076, 267920, 279756, 275200, 259500, 283272, 275100, 251328, 231516, 249912, 245588, 256320, 241092, 248976, 234240, 239936, 227180, 252960, 213180, 241392, 232092, 235600, 234548, 213504, 240864, 233576, 204360, 202272, 210396, 222552, 206960, 216800, 206628, 198768, 190820, 196656, 200080, 234016, 218592, 196352, 207328, 195720, 207624, 184864, 189996, 173768, 184040, 203904, 188356, 226720, 165564, 168080, 146744, 156288, 165912, 166656, 178200, 154584, 157084, 149568, 162132, 161920, 166320, 150336, 167760, 153504, 155100, 147264, 152628, 133280, 130972, 155520, 147492, 167464, 138996, 160064, 135240, 132840, 137332, 127968, 127488, 134000, 111444, 134064, 129536, 129032, 106080, 109568, 103828, 122808, 97384, 121680, 110664, 107944, 111512, 97152, 121900, 122360, 90780, 99696, 79624, 179280, 105148, 97920, 103740, 95352, 79200, 86112, 113016, 106752, 104904, 91840, 282124, 109416, 101880, 90880, 107160, 106392, 118244, 130176, 109820, 95120, 109416, 91104, 97276, 103488, 135700, 157472, 90288, 97744, 100464, 78000, 67424, 94224, 88476, 93632, 96380, 97920, 116660, 167552, 117420, 102920, 84592, 113568, 90144, 97968, 79380, 60672, 87492, 66144, 84216, 75520, 91164, 64400, 67184, 72576, 76700, 70416, 61476, 77408, 76328, 64680, 82088, 91632, 69264, 81496, 71020, 55104, 59312, 58136, 86784, 58480, 76384, 84816, 67228, 53664, 55200, 69200, 77728, 72384, 78176, 54600, 63180, 64768, 80484, 70800, 78100, 75472, 58548, 51552, 68928, 51840, 67868, 55024, 39204, 56784, 70080, 55632, 64592, 58880, 81180, 69560, 77168, 53568, 55204, 58344, 58500, 55648, 49764, 52920, 56092, 54720, 48768, 55008, 44428, 44544, 40040, 60216, 38700, 71392, 52904, 34320, 50048, 58016, 40872, 64616, 67940, 33264, 73048, 52536, 60648, 48000, 43308, 28944, 46748, 50096, 43740, 34104, 48840, 26112, 35992, 54120, 36168, 44496, 23128, 44712, 39840, 44928, 43368, 45144, 45252, 33600, 67360, 42200, 55836, 47488, 34000, 35784, 44408, 39376, 37752, 27520, 41376, 38016, 38104, 31248, 36540, 40112, 31464, 40296, 35120, 51040, 52920, 21216, 28352, 37296, 42720, 33896, 32184, 25088, 43104, 39600, 39688, 43392, 48924, 45400, 40040, 60192, 31076, 42136, 42228, 49680, 35036, 53592, 48152, 48256, 48360, 27960, 42964, 35568, 30016, 43240, 39564, 54752, 39732, 43608, 32300, 51408, 17172, 45888, 42152, 40320, 19240, 50128, 30912, 42592, 31040, 19440, 19480, 35136, 44988, 27440, 37316, 33456, 45356, 33592, 35640, 27776, 13916, 31872, 23952, 28000, 26052, 30120, 26156, 24192, 16160, 26312, 28392, 26416, 18324, 26520, 26572, 20480, 22572, 20560, 30900, 16512, 35156, 29008, 24912, 22880, 16672, 27144, 16736, 25152, 23100, 35768, 29512, 16896, 40204, 40280, 36108, 40432, 38376, 19224, 27820, 27872, 21480, 10760, 21560, 34560, 21640, 21680, 28236, 19584, 10900, 21840, 35008, 19728, 13176, 30800, 19836, 30912, 11060, 17728, 33300, 22240, 17824, 35712, 22360, 15680, 26928, 13488, 20268, 24816, 29380, 18112, 11340, 20448, 29588, 18240, 27408, 9152, 22920, 34440, 23000, 25344, 30004, 23120, 16212, 6960, 18592, 20952, 25652, 21024, 16380, 28128, 30524, 16464, 11780, 23600, 18912, 33152, 9488, 19008, 30940, 9536, 11940, 19136, 11980, 19200, 19232, 16856, 21708, 33824, 12100, 19392, 12140, 21888, 26796, 19520, 26884, 14688, 17164, 29472, 19680, 24640, 17276, 19776, 34664, 29760, 7452, 19904, 14952, 12480, 32500, 5008, 35112, 20096, 22644, 27720, 30288, 32864, 15192, 12680, 22860, 20352, 10192, 28072, 20448, 30720, 20512, 30816, 12860, 30912, 25800, 46512, 25880, 25920, 23364, 18200, 31248, 15648, 47016, 15696, 36680, 15744, 23652, 31584, 13180, 31680, 34372, 31776, 34476, 18592, 18620, 31968, 32016, 34736, 29436, 29480, 29524, 13440, 24228, 35048, 27000, 32448, 24372, 24408, 29876, 24480, 24516, 16368, 16392, 21888, 43840, 32928, 43968, 24768, 19292, 35880, 24876, 35984, 36036, 13880, 25020, 36192, 27880, 22336, 53124, 22400, 14020, 28080, 28120, 39424, 33840, 14120, 28280, 33984, 28360, 31240, 28440, 31328, 14260, 25704, 40040, 34368, 31548, 34464, 31636, 11520, 34608, 17328, 43380, 17376, 26100, 23232, 52344, 37856, 11664, 35040, 11696, 11712, 5864, 20552, 23520, 20608, 23584, 17712, 20692, 29600, 26676, 38584, 29720, 20832, 17880, 5968, 17928, 5984, 8988, 15000, 6008, 3008, 6024, 9048, 6040, 3024, 3028, 3036, 6088, 6104, 3056, 3060, 3068, 6144, 3076, 3080, 6176, 3092, 3096, 3100, 3104, 3108, 6224, 3116, 6240, 3124, 3128, 3132, 3136, 3140, 3160, 3164, 3172, 3176, 3192, 9588, 6400, 6408, 3212, 6432, 3224, 3228, 3232, 3240, 3248, 3252, 3256, 6528, 6560, 3284, 6592, 3300, 3304, 3308, 3316, 3320, 3332, 3352, 3376, 3388, 3412, 3420, 6856, 3456, 3484, 3488, 10476, 3496, 3500, 3512, 3516, 7040, 3532, 3536, 3540, 7112, 3560, 7144, 3588, 3596, 3600, 3612, 3616, 3624, 3640, 3676, 3696, 7408, 3716, 3764, 3772, 3812, 3824, 7664, 3836, 3840, 3848, 3852, 3864, 3872, 3876, 3884, 3896, 3900, 11712, 3920, 3928, 7872, 3940, 3944, 3948, 7904, 3956, 7944, 11928, 3980, 11952, 7984, 7992, 8040, 4028, 4048, 8240, 4200, 4208, 4268, 8600, 4344, 4392, 4416, 4464, 4504, 4536, 4572, 4584, 4692, 4820, 4860, 4900, 4912, 4920, 4968, 5012, 5064, 5152, 5376, 5432, 5476, 5484, 5644, 5868, 5992, 6068, 6224, 6228, 6276, 6308, 6352, 7184, 7308, 7404, 7432, 7904, 7988, 9284, 9504, 9988, 10336, 11316, 11576, 13060, 18288, 19032, 19516, 22388, 32720, 33712, 52200, 60652, 81172)
measure_burst=(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
        16384, 32768, 65536, 131072, 262144, 524288, 1048576)
measure_lat=(99.69, 60.973, 31.8107,23.1651,13.873,11.0905,10.8282, 10.7025, 10.637, 10.6059, 10.5901,
        6.39104, 4.59523, 3.70911,3.26604,3.04413,2.93171,2.87666,2.84858,2.83507,2.82805)
index = 0
estimated_lat = []
while(index < len(burst_len)):
    i = 0;
    while(burst_len[index] > measure_burst[i] and i < len(measure_burst) - 1):
        i = i + 1
    if(burst_len[index] == measure_burst[i]):
        lat = measure_lat[i]
    else:
        slope = (measure_lat[i-1] - measure_lat[i])/(measure_burst[i] - measure_burst[i-1])
        lat = measure_lat[i-1] - slope * (burst_len[index] - measure_burst[i-1])
    lat = lat * transfer_amount[index]
    estimated_lat.append(lat)
    index = index + 1

total_access_time = sum(estimated_lat)
accumulated_lat_percent=[]
accumulated_lat = 0.0
for lat in estimated_lat:
    accumulated_lat += lat;
    accumulated_lat_percent.append(accumulated_lat/total_access_time)

plt.loglog(burst_len, burst_freq, 'bo', label='Burst Distribution')
#plt.loglog(burst_len, transfer_amount, 'rs', label='Amount of Transfer')
#plt.semilogy(burst_len, burst_freq, 'bo')
ax.set_xlabel('Burst Length')
ax.set_ylabel('# of Bursts')

ay = ax.twinx()
ay.plot(burst_len, accumulated_lat_percent, 'r^-', label='Memory Access Proportion')
#ay.semilogy(burst_len, transfer_amount, 'ro')
ay.set_ylabel('Accumulated Proportion of Memory Access Time')

lx, labelx = ax.get_legend_handles_labels()
ly, labely = ay.get_legend_handles_labels()
ay.legend(lx + ly, labelx + labely, loc='right')

plt.tight_layout()
#plt.show()
#fig.set_size_inches(8, 6)
plt.savefig("../burst_len_lj.pdf", bbox_inches='tight', )
