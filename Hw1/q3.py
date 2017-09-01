import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def step():
    x = random.random() * 1.5
    if x < 0.25:
        return (0, -1, 0)
    if x < 0.5:
        return (0, 1, 0)
    if x < 0.75:
        return (1, 0, 0)
    if x < 1:
        return (-1, 0, 0)
    if x < 1.25:
        return (0, 0, -1)
    if x < 1.5:
        return (0, 0, 1)
def rw(s):
    init = (0, 0, 0)
    path_x = []
    path_y = []
    path_z = []
    steps = s
    for i in range(steps):
        path_x.append(init[0])
        path_y.append(init[1])
        path_z.append(init[2])
        init = np.add(init, step())
    return (path_x, path_y, path_z)
'''
px, py, pz = rw(1000)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(px, py, pz)
plt.show()
'''

