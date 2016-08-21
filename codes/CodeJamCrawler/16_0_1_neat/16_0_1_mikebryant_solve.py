#!/usr/bin/env python

T = int(raw_input().strip())

def calc(N):
    if N == 0:
        return 'INSOMNIA'
    seen = set()
    for i in range(1, 10000000):
        n = i * N
        seen |= set(str(n))
        if len(seen) == 10:
            return n
    return 'INSOMNIA-OUTOFNUMS'


for i in range(1, T+1):
    print ("Case #%d:" % i),
    N = int(raw_input().strip())
    print calc(N)
