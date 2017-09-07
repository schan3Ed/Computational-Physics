import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize as opt

def step(history, i, j):
    left = history[i - 1][j]
    right = history[i + 1][j]
    up = history[i][j + 1]
    down = history[i][j - 1]
    p = left + right + up + down
 #   print p
    rand = random.random() * p
  #  print rand
    if rand < left:
        return (-1, 0)
    if rand < left + right:
        return (1, 0)
    if rand < left + right + up:
        return (0, 1)
    if rand < left + right + up + down:
        return (0, -1) 
    return (-1, -1) 

def saw(n):
    board = np.ones((2 * n + 2, 2 * n + 2))
    history = board
    a = n + 1 
    b = n + 1
    path_x = []
    path_y = []
    path_x.append(0)
    path_y.append(0)
    history[a][b] = 0
    for i in range(n):
        x, y = step(history, a, b)
        if x == -1 and y == -1:
            '''
            plt.plot(path_x, path_y)
            plt.title("SAW that is stuck while generating steps 300")
            plt.show()
            '''
            return "stuck"
        a += x
        b += y
        history[a][b] = 0
        path_x.append(a - n - 1)
        path_y.append(b - n - 1)
    '''
    if n == 99:
        plt.plot(path_x, path_y)
        plt.title("SAW with steps of 99")
        plt.show()
        print len(path_x)
    '''
    return path_x, path_y
       # print history

        
    
   # print board
l = []
l_m = []
n = 100
trials = 100
for i in range(4, n):
    j = 0
    print "Doing steps #: ", i
    while j < trials:
    #    print j 
        x = saw(i)
        if x == "stuck":
            print "j: ", j
            j = j - 1
        else:
            dist = (x[0][-1] - i - 1) ** 2 + (x[1][-1] - i - 1) ** 2
           # print x[0][-1], "    ", x[1][-1]
            l.append(dist)
        j += 1
    l_m.append(np.array(l).mean())
#print l_m
l_m = np.array(l_m)
x = np.array(range(4, n))
plt.plot(np.log(x), np.log(l_m))
plt.xlabel("steps")
plt.ylabel("<r^2>")
plt.title("<r^2> of SAW vs steps")
#plt.show()
plt.xlabel("ln(steps)")
plt.ylabel("ln(<r^2>)")

x, y = opt.curve_fit(lambda t,a,b: a + 2 * b * t, np.log(x)[1:40], np.log(l_m)[1:40])
plt.title("ln(<r^2>) of SAW vs ln(steps) with slope: " + str(round(x[1], 2)))
plt.text(2, 7, "steps: " + str(n) + " trials: " + str(trials))
print x[0], "   ",  x[1]
print np.sqrt(np.diag(y))
#for i in range(4, n, 2):
 #   plt.scatter(i, x[0] + 2 * x[1] * i)
plt.show()
#plt.plot([10, 20, 30, 40, 50, 70], [.52, .62, .68, .71, .75, .79])
#plt.show()


