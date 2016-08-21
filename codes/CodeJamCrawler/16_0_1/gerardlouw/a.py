#!/usr/bin/env python3

def solve(N):
    if N == 0:
        return "INSOMNIA"
    n = 0
    seen = set()
    while len(seen) < 10:
        n += N
        seen |= set(str(n))
    return n

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print("Case #%d: %s" % (t, solve(N)))
