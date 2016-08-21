#!/usr/bin/env python3

import heapq
import sys

def solve(P):
    remaining = sum(P)
    results = []
    P = list((-x, p) for x, p in zip(P, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    heapq.heapify(P)
    while remaining > 0:
        if -P[0][0] * 2 < remaining:
            p = heapq.heappop(P)
            results.append(p[1])
            remaining -= 1
            if p[0] != -1:
                heapq.heappush(P, (p[0]+1, p[1]))
        else:
            p1 = heapq.heappop(P)
            p2 = heapq.heappop(P)
            results.append(p1[1]+p2[1])
            remaining -= 2
            if p1[0] != -1:
                heapq.heappush(P, (p1[0]+1, p1[1]))
            if p2[0] != -1:
                heapq.heappush(P, (p2[0]+1, p2[1]))

    print(*results)
    sys.stdout.flush()


if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        input()
        P = [int(x) for x in input().split()]
        print('Case #{}: '.format(i), end='')
        solve(P)
