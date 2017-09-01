import numpy
import math
import matplotlib.pyplot as plt


def fx(p):
    return math.sin(p) / math.sqrt(p)


def trap(N, b, a):
    h = float(b - a) / N
    sum = 0
    for k in range(1, N - 1):
        xk0 = a + k * h
        xk1 = a + (k + 1) * h
        sum += fx(xk0) + fx(xk1)
    print "Error for this iteration:  ", math.pow(h, 3)
   # print sum
    return float(h) / 2 * sum

for i in range(1, 200):
    plt.scatter(i * 0.1, trap(200, i * 0.1, 0 ))
  #  print trap(10, i, 0 )
plt.show()