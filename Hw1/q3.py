import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from scipy import optimize as opt

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
def rw(s, path):
    init = (0, 0, 0)
    for i in range(s):
        path.add(init)
        st = step()
        init = (init[0] + st[0], init[1] + st[1], init[2] + st[2])
       # print len(path)
    print len(path)
    return path

def rw_2(s):
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


l = []
points = set()
for i in range(3):
    print "trial #: ", i
    points = rw(10000, points)
    for point in points:
        l.append(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)

#print l
#print points
num_dist = []
l = np.sqrt(np.array(l))
l.sort()
print l
for r in range(1, 20):
    num_dist.append(sum(i < r for i in l))
print num_dist
num_dist = np.log(np.array(num_dist))[1:10]
print num_dist
x = np.log( range(1, 10))

fit, err = opt.curve_fit(lambda a, b, t: a + b * t, x, num_dist)
print fit

plt.title("ln(N within r) vs ln(r) with a slope of " + str(round(fit[1], 2)))
plt.xlabel("ln(r)")
plt.ylabel("ln(N)")
plt.plot(x, num_dist)
plt.show()

#To show a single random walk
'''
px, py, pz = rw_2(10000)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(px, py, pz)
plt.title("Random walk in 3d with 10000 steps")
plt.show()
'''

