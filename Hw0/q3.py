import copy
import random
from collections import deque
import math

def rec(head, tail, all_list):
    if(len(tail) < 1):
        all_list.append(head)
        return
    for i in range(len(tail)):
        x = tail[i]
        po = copy.copy(tail)
        po.pop(i)
        p = list(head)
        p.append(x)
      #  tail.append(x)
#       print(p, "    ", round_count, "   ", tail, "   ", i)
        rec(copy.copy(p), po, all_list)

x = random.random()
pairs = []
#print(x)

for i in range(7):
    x = random.random()
    y = random.random()
    x = round(x, 2)
    y = round(y, 2)
    pair = []
    pair.append(x)
    pair.append(y)
    pairs.append(pair)

perm_pairs = []


print("This is a set of paris    \n", pairs)

rec([], pairs, perm_pairs)


for i in range(7):
    print(perm_pairs[i], '\n')

for pairs in perm_pairs:
    sum = 0
    for i in range(0, len(pairs) - 2, 2):
     #   print(pairs[i])
        x1 = pairs[i][0]
        y1 = pairs[i][1]
        x2 = pairs[i + 1][0]
        y2 = pairs[i + 1][1]
        
        sum += math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    pairs.insert(0, sum)    
perm_pairs.sort()

for i in range(10):
    print(perm_pairs[i], "\n")
        
