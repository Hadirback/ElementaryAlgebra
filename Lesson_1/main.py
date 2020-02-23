# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
# X, Y = np.meshgrid(X, Y)
Z = 2*X + 5*Y
# ax.plot_wireframe(X, Y, Z)
# ax.scatter(0, 0, 0, 'z', 50, 'red')
ax.plot(X, Y, Z, 'red')
ax.plot(X, Y, Z * Z, 'red')
show()
