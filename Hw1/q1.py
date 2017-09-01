import random
import matplotlib.pyplot as plt
import numpy

def gen():
    sum = 0
    for i in range(12):
        sum += random.random()
    return sum

all_x = []
times = 100000
for x in range(times):
    all_x.append(gen())
#print all_x
n = numpy.array(all_x)
mean = n.mean()
var = numpy.var(n)
print mean, "      ", var
plt.hist(all_x, bins=48, range=[0, 12])
plt.show()
