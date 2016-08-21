#!/usr/bin/env pypy3

import sys

sols = []
sols.append({'P': 'P', 'S': 'S', 'R': 'R'})
for i in range(1, 13):
    res = dict()
    choices = 'PSR'
    for c in choices:
        attempt1 = ''.join(sols[i-1][t] for t in filter(lambda x: x!=c, choices))
        attempt2 = ''.join(sols[i-1][t] for t in filter(lambda x: x!=c, choices[::-1]))
        if attempt1 < attempt2:
            res[c] = attempt1
        else:
            res[c] = attempt2
    sols.append(res)

def solve():
    N, R, P, S = map(int, input().split())
    best = None
    for c in 'PSR':
        r_c = sum(1 if x == 'R' else 0 for x in sols[N][c])
        p_c = sum(1 if x == 'P' else 0 for x in sols[N][c])
        s_c = sum(1 if x == 'S' else 0 for x in sols[N][c])
        if r_c == R and p_c == P and s_c == S:
            if best is None or best > sols[N][c]:
                best = sols[N][c]
    return best

T = int(input())
for l in range(1, T+1):
    print("Case #%d:" % l, end=" ")
    res = solve()
    print(res if res is not None else "IMPOSSIBLE")
