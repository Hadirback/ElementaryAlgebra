# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 201)
y = 3*x + 1
y2 = -(1/3)*x + 1

plt.plot(x, y)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-5, 5)

plt.grid(True)
plt.show()