#!/usr/bin/python

import sys

def decompose(k):
    while k != 0:
        k, r = k // 10, k % 10
        yield r

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    se = set()
    k = 0
    while True:
        k += n
        for x in decompose(k):
            se.add(x)
        if len(se) == 10:
            break
    return k

T = int(input())
for t in range(T):
    N = int(input())
    ans = solve(N)
    print('Case #{}: {}'.format(t + 1,  ans))

