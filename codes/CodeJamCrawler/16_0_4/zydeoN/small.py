#!/usr/bin/env python3

from itertools import product
import sys

from numpy import float64   # so that float64(1)/0 == inf (avoid errors)
inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def small(K, C, S):
    return range(1, K+1)

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        K, C, S = read_ints()
        ans = small(K, C, S)
        if ans == []:
            print("Case #%d: IMPOSSIBLE" % (tc))
        else:
            print("Case #%d: " % tc, end="")
            for a in ans:
                print(a, end=" ")
            print("")
