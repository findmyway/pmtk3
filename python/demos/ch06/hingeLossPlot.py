#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as pl

x = np.arange(-2, 2, 0.01)
L01 = x < 0
Lhinge = np.where(x > 1, 0, 1 - x)
Lexp = np.exp(-x)
Llog = np.log2(1 + Lexp)

#plot
pl.plot(x, L01, 'k-', label='0-1')
pl.plot(x, Lhinge, 'r--', label='hinge')
pl.plot(x, Lexp, 'b-.', label='exp')
pl.plot(x, Llog, 'g--', label='log')
pl.legend()
pl.show()
pl.savefig('hingeLossPlot.png')
