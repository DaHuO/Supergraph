#!/usr/bin/env python3
import numpy
import sys
def f(K, C, S):
    '''
    gold tile in position k out of K means that any number in base K
    if it has a digit with value k, will have gold
    '''
    if S*C < K:
        return None
    n = (K + (C - 1)) // C
    arr = numpy.arange(n*C, dtype=int).reshape((n, C))
    a2 = numpy.power(K, numpy.arange(C))
    arr *= (arr < K)
    arr *= a2
    nums = arr.sum(1) + 1
    return set(nums)

n = int(sys.stdin.readline())
for i in range(n):
    k, c, s = list(map(int, sys.stdin.readline().split()))

    # res = f(k, c, s)
    res = list(range(1, k+1))
    if res is None:
        res = 'IMPOSSIBLE'
    else:
        res = ' '.join(str(i) for i in res)
    print("Case #%d: %s" % ((i+1), res))
