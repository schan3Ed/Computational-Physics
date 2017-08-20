from collections import deque
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
        print(p, "    ", round_count, "   ", tail, "   ", i)
        rec(copy.copy(p), copy.copy(tail), round_count - 1, all_list, var)



tail = deque([1, -1])
head = deque([])
round_count = 4
var = 2
all_list = []
rec(head, tail, round_count, all_list, var)
print(all_list)
        