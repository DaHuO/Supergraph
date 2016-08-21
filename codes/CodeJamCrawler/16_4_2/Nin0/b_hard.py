#!/usr/bin/python3

from itertools import *
import sys
import random

def get_tie(p):
    results = {(0, 0): 1}  # (yes, no): probability
    cnt = 0
    for x in p:
        cnt += 1
        new_res = {(i, cnt - i): 0.0 for i in range(0, cnt + 1)}
        # print(new_res)
        for (y, n), prob in results.items():
            new_res[(y + 1, n)] += results[(y, n)] * x
            new_res[(y, n + 1)] += results[(y, n)] * (1.0 - x)
        results = new_res
    k = len(p) // 2
    return results[(k, k)]

def quick_solve(n, k, p):
    best = 0
    for i in range(0, k + 1):
        left = p[:i]
        right = p[len(p) - k + i:]
        # print(left, right)
        t = get_tie(left + right)
        if t > best:
            best = t
    return best

t = int(sys.stdin.readline())
for testCase in range(1, t + 1):
    n, k = [int(x) for x in sys.stdin.readline().split()]
    p = sorted([float(x) for x in sys.stdin.readline().split()])
    prob = quick_solve(n, k, p)
    print('Case #{0}: {1}'.format(testCase, prob))
