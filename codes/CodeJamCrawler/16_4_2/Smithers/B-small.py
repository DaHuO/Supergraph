#!/usr/bin/env python3

# Google Code Jam Round 2 2016
# Problem B. Red Tape Committee
# Solution in Python
# By Smithers

import itertools

for x in range(1, int(input()) + 1):
    n, k = (int(_) for _ in input().split())
    
    p = [float(_) for _ in input().split()]
    
    y = 0
    for committee in itertools.combinations(p, k):
        temp = [0] * (k + 1)
        temp[0] = 1
        for prob in committee:
            for i in range(k, 0, -1):
                temp[i] = temp[i] * (1 - prob) + temp[i-1] * prob
            temp[0] = temp[0] * (1 - prob)
        if temp[k // 2] > y:
            y = temp[k // 2]
    
    print('Case #' + str(x) + ':', y)
