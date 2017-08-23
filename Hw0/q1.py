import scipy as scipy
import numpy as numpy

def multiply(ma, mb):
    n = ma.ndim
    mc = numpy.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                mul = 1
                if (i + j + k) % 2 == 1:
                    mul = -1
                sum += ma[i, k] * mb[k, j] * mul
            mc[i, j] = sum
    return mc

#example
ma = numpy.matrix('1 1; 1 1')
mb = numpy.matrix('1 1; 1 1')
print(multiply(ma, mb))

#solved
