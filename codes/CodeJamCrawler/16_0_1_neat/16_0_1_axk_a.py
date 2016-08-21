#!/usr/bin/env python3

def calc(N):
    if N == 0:
        return 'INSOMNIA'
    n = 0
    seen = set()
    while True:
        n += N
        seen |= {int(d) for d in str(n)}
        if len(seen) == 10:
            return n

T = int(input())
for t in range(T):
    N = int(input())
    r = calc(N)
    print("Case #{}: {}".format(t + 1, r))
