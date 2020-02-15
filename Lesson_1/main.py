import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y1 = np.cos(x)
y2 = np.cos(2 * x)
plt.plot(x, y1, x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
