#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]
C = [5, 10, 20, 30]

X = range(4)

plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'r', bottom = A)
plt.bar(X, C, color = 'y', bottom = np.array(B) + np.array(A))
plt.show()
