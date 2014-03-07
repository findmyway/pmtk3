#!/usr/bin/env python

import matplotlib.pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from utils import load_mat

data = load_mat('moteData')
X = data['X']
y = data['y']

fig1 = pl.figure()
ax1 = fig1.add_subplot(111, projection='3d')
fig2 = pl.figure()
ax2 = fig2.add_subplot(111, projection='3d')
#plot points
ax1.scatter(X[:, 0], X[:, 1], y)
ax2.scatter(X[:, 0], X[:, 1], y)

#linear
x = np.c_[np.ones(X.shape[0]), X]
w = np.linalg.lstsq(x, y)[0]
#plot linear surface
x1_range = np.linspace(np.min(X[:, 0]), np.max(X[:, 1]), 100)
x2_range = np.linspace(np.min(X[:, 0]), np.max(X[:, 1]), 100)
xx1, xx2 = np.meshgrid(x1_range, x2_range)
z = w[0] + w[1] * xx1 + w[2] * xx2  # broadcast
ax1.plot_surface(xx1, xx2, z, cmap=cm.coolwarm)
fig1.savefig('surfaceFitDemo_linear.png')

# quadratic
x = np.c_[np.ones(X.shape[0]), X, X ** 2]
w = np.linalg.lstsq(x, y)[0]
#plot quadratic surface
z = w[0] + w[1] * xx1 + w[2] * xx2 + w[3] * (xx1 ** 2) + w[4] * (xx2 ** 2)
ax2.plot_surface(xx1, xx2, z, cmap=cm.coolwarm)
fig2.savefig('surfaceFitDemo_quadratic.png')

pl.show()
