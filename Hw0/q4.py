import numpy
import math


def fx(p):
    return numpy.sin(p) / numpy.sqrt(p)


def trap(N, b, a):
    h = (b - a) / N
    sum = 0
    for k in range(N - 1):
        xk0 = a + k * h
        xk1 = a + (k + 1) * h
        sum += fx(xk0) + fx(xk1)
    print math.pow(h, 3)
    return h / 2 * sum

trap(10, 3, 2)