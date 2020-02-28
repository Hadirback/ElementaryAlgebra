import numpy as np

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

rads = np.arange(0, (2*np.pi), 0.01)
plt.axes(projection='polar')
plt.yticks(np.arange(-2,2,0.5))
for radian in rads:
    plt.polar(radian, 3, 'o')
plt.show()