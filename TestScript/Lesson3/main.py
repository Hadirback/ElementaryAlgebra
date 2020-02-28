import numpy as np
import matplotlib.pyplot as plt


def func_circle(x, radius):
    return np.sqrt(radius**2 - x**2)


def func_ellipse(x, a, b):
    return b * np.sqrt(1 - x**2/a**2)


def func_hyperbola(x, a, b):
    return b * np.sqrt(x**2/a**2 - 1)


fig, ax = plt.subplots(nrows=3, ncols=1)
plt.subplots_adjust(hspace=0.40)
radius = 5
x = np.linspace(-5, 5, 1000)
ax[0].set_title('Окружность')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_xlim(-10, 10)
ax[0].plot(x, func_circle(x, radius))
ax[0].plot(x, -func_circle(x, radius))

ax[0].grid(True, which='both')

x = np.linspace(-3, 3, 1000)
ax[1].set_title('Эллипс')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_xlim(-4, 4)
ax[1].plot(x, func_ellipse(x, 3, 2))
ax[1].plot(x, -func_ellipse(x, 3, 2))
ax[1].grid()

x = np.linspace(-5, 5, 1000)
ax[2].set_title('Гипербола')
ax[2].set_xlabel('x')
ax[2].set_ylabel('y')

ax[2].set_xlim(-4, 4)
ax[2].plot(x, func_hyperbola(x, 1, 2))
ax[2].plot(x, -func_hyperbola(x, 1, 2))
ax[2].grid()
fig.set_figheight(14)
plt.show()