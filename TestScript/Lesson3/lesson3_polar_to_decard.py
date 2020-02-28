import numpy as np


def convert_to_cartesian_coordinates(alfa, radius):
    x = radius * np.cos(alfa)
    y = radius * np.sin(alfa)
    return x, y


x1, y1 = convert_to_cartesian_coordinates(np.pi, 3)
print(x1, " ", y1)