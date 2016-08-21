#!/bin/python3
import math
import numpy as np

def solve(s):
    chars = list(s)
    arr = np.array([-1 if c == '-' else 1 for c in chars][::-1])
    num_flips = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            num_flips += 1
            arr *= -1
    return num_flips

num_cases = int(input())
for casenum in range(1, num_cases+1):
    s = raw_input()
    res = solve(s)
    print ("Case #{0}: {1}".format(casenum, res))
