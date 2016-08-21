#!/usr/bin/python

import sys
from collections import Counter

def solve2(d, cnt):
    if cnt == 0:
        return ''

    items = sorted(d.items(), key=lambda x:x[1], reverse=True)
    ans = items[0][0]
    d[items[0][0]] -= 1
    if items[1][1] * 2 > cnt - 1:
        ans += items[1][0]
        d[items[1][0]] -= 1
    cnt -= len(ans)

    delim = ' ' if cnt != 0 else ''
    return (ans + delim, d, cnt)

def solve(N, arr):
    d = Counter()
    cnt = 0
    for i, k in enumerate(arr):
        c = chr(ord('A') + i)
        d[c] += k
        cnt += k

    ans = ''
    while cnt != 0:
        a, d, cnt = solve2(d, cnt)
        ans += a
    return ans

T = int(input())
for t in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    ans = solve(N, arr)
    print('Case #{}: {}'.format(t + 1,  ans), flush=True)

