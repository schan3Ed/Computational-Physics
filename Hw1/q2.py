import random
import numpy as np
import matplotlib.pyplot as plt
import math

def step():
    x = random.random()
    if x < 0.25:
        return (0, -1)
    if x < 0.5:
        return (0, 1)
    if x < 0.75:
        return (1, 0)
    return (-1, 0)

def rw(s):
    init = (0, 0)
    path_x = []
    path_y = []
    steps = s
    for i in range(steps):
        path_x.append(init[0])
        path_y.append(init[1])
        init = np.add(init, step())
    return (path_x, path_y)

pts = []
for i in range(1, 70):
    print "Doing walk #:  ", i
    p = []
    for j in range(500):
        px, py = rw(i)
        dist = px[-1] ** 2 + py[-1] ** 2
        p.append(dist)
    pts.append(np.array(p).mean())

plt.plot(pts)
plt.show()
#px, py = rw(10000)
    #print path_y
#plt.plot(0, 0, marker='o')
#plt.plot(px, py )
#plt.plot(px[-1], py[-1], marker='o')
#plt.axis([s * -1, s, s * -1, s])
#plt.show()