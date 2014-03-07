#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as pl

lams = [0.1, 0.4, 0.5, 0.6]  # decent step
iters = 30  # iter times


def fn(x):
    """common function"""
    return (0.5 * (x[0] ** 2 - x[1]) ** 2 +
            0.5 * (x[0] - 1) ** 2)


def fn_der(x):
    """first derivative of fn"""
    x0_der = (x[0] ** 2 - x[1]) * 2 * x[0] + (x[0] - 1)
    x1_der = -(x[0] ** 2 - x[1])
    return np.array((x0_der, x1_der))

#draw contours
x = np.linspace(0, 2, 100)
y = np.linspace(-0.5, 3, 100)
xx, yy = np.meshgrid(x, y)
z = fn((xx.ravel(), yy.ravel()))
z = z.reshape(xx.shape)
levels = np.hstack((np.arange(0, 0.5, 0.05), np.arange(1, 10, 0.5)))


for lam in lams:
    pl.figure()
    pl.contour(xx, yy, z, levels=levels)
    xy_old = np.array([0, 0])
    pl.plot(xy_old[0], xy_old[1], 'ro')
    for i in range(iters):
        xy_der = fn_der(xy_old)
        xy_new = xy_old - lam * xy_der
        point_x, point_y = zip(xy_old, xy_new)
        pl.plot(point_x, point_y, 'b-')
        pl.plot(xy_new[0], xy_new[1], 'ro')
        xy_old = xy_new


pl.show()
