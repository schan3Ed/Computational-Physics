import matplotlib.pyplot as plt
import random


def prob(n, l):
    for i in range(n):
        for j in range(n):
            x = random.random()
            if(x < 0.3333333):
                l[i][j] = 1

def lattice(n, l):
    for i in range(n):
        l.append([])
        for j in range(n):
            l[i].append(0)

def plot(n, l):
    for i in range(n):
        for j in range(n):
            if (l[i][j] == 1) :
                str = "red"
            else:
                str = "none"
            plt.scatter(i, j, marker="o", facecolors=str)
    plt.show()

l = []
lattice(20, l)
prob(20, l)
plot(20, l)

