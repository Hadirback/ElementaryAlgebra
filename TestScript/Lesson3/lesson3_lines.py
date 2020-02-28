import numpy as np
import matplotlib.pyplot as plt

k1 = 1
b1 = 2
a1 = np.pi/2

k2 = 3
b2 = 1
a2 = np.pi/3

x = np.linspace(-20, 20, 100)
y1 = k1 * np.cos(x - a1) + b1
y2 = k2 * np.cos(x - a2) + b2
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot([-10, 10],[0,0], color ='red', linewidth=0.75, linestyle ="--")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()