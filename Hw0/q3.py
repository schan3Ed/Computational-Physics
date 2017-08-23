import numpy as numpy
import random
import copy

def rec(head, tail, round_count, all_list, var):
    if(round_count < 1):
        all_list.append(head)
        return
    for i in range(var):
        x = tail.popleft()
        p = list(head)
        p.append(x)
        tail.append(x)
#        print(p, "    ", round_count, "   ", tail, "   ", i)
        rec(copy.copy(p), copy.copy(tail), round_count - 1, all_list, var)


for i in range(7):
    x = random()
    y = random()

