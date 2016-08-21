#!/usr/bin/env python3

import sys
from collections import *

def print_sol(tc, ans):
    print('Case #{}: {}'.format(tc, ans))

T = int(input())
for tc in range(1, T+1):
    N, K = [int(x) for x in input().split(' ')]
    P = [float(x) for x in input().split(' ')]

    assert len(P) == N

    probs = []

    result = 0.0

    for i in range(1<<N):
        if bin(i).count("1") != K:
            continue

        px = [P[b] for b in range(N) if (i & (1<<b)) != 0]

        cur = [0] * (K//2+1)
        cur[0] = 1
        for k in range(K):
            nxt = [0] * (K+1)
            for y in range(0, K//2 + 1):
                nxt[y+1] += cur[y] * px[k]
                nxt[y] += cur[y] * (1 - px[k])

            cur = nxt

        result = max(result, nxt[K//2])

    print_sol(tc, result)
