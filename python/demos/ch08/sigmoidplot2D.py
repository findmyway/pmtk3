#!/usr/bin/env python

import matplotlib.pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid.axislines import SubplotZero

w_1 = np.array([-2, -2, 0, 1, 1, 2,  2, 3, 5, 5])
w_2 = np.array([-1,  3, 2, 4, 0, 2, -2, 0, 4, 1])


def sigmoid(x):
    return 1.0 / (1 + np.exp(x))


fig = pl.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-3, 6])
ax.set_ylim([-3, 6])
ax.grid()

for w1, w2 in zip(w_1, w_2):
    ax_x = fig.add_axes([(w1 + 4) / 12.0, (w2 + 4) / 12.0,
                         0.15,  0.15],
                        projection='3d')
    x = np.linspace(-1, 1, 100)
    x1, x2 = np.meshgrid(x, x)
    z = sigmoid(w1 * x1 + w2 * x2)
    ax_x.plot_surface(x1, x2, z, cmap='hot')
    ax_x.set_title('w = (%d,%d)' % (w1, w2))
    ax_x.w_xaxis.set_ticklabels([])
    ax_x.w_yaxis.set_ticklabels([])
    ax_x.w_zaxis.set_ticklabels([])

pl.savefig('sigmoidplot2D.png')
pl.show()
