#!/usr/bin/env python

import matplotlib.pylab as pl
import numpy as np

n = 10  # samples

#gengerate random points
x = np.random.randn(n)
y = 1 + x + np.random.randn(n) * 0.3
y_real = x + 1

#fit them
x_extern = np.vstack((np.ones(n), x)).T
w = np.linalg.lstsq(x_extern, y.T)[0]
y_est = w[0] + w[1] * x

pl.scatter(x, y, c='r', marker='o')
pl.scatter(x, y_est, c='b', marker='x')

x_range = np.linspace(x.min() - 1, x.max() + 1, 100)
y_real_range = x_range + 1
y_est_range= w[0] + x_range * w[1]
pl.plot(x_range, y_real_range, 'b--', label='true')
pl.plot(x_range, y_est_range, 'r-', lw=3, label='prediction')

for i in range(n):
    pl.plot((x[i], x[i]), (y[i], y_est[i]), 'b', lw=3)
pl.legend()
pl.grid()
pl.savefig('residualsDemo.png')
pl.show()
