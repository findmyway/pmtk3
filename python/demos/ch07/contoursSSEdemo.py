#!/usr/bin/env python

import matplotlib.pylab as pl
import numpy as np

n = 10  # samples

#gengerate random points
x = np.random.randn(n)
y = 1 + x + np.random.randn(n) * 0.3

#fit them
x_extern = np.vstack((np.ones(n), x)).T
w = np.linalg.lstsq(x_extern, y.T)[0]

w_x = np.linspace(w[0] - 1, w[0] + 1, 100)
w_y = np.linspace(w[1] - 1, w[1] + 1, 100)
w_xx, w_yy = np.meshgrid(w_x, w_y)
W = np.vstack((w_xx.ravel(), w_yy.ravel())).T
err = np.dot(W, np.vstack((np.ones(n), x))) - y
squared_err = np.sum(err * err, axis=1)

pl.contour(w_xx, w_yy, squared_err.reshape(w_xx.shape))
pl.scatter(w[0], w[1], c='r', marker='x', s=50)
pl.savefig('contoursSSEdemo.png')
pl.show()
