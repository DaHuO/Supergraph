#!/usr/bin/env python3

def first(n):
    s = set()
    x = 0
    while len(s) < 10:
        x += n
        for d in str(x):
            s.add(d)
    return x


T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    print("Case #{}: {}".format(t, first(N) if N > 0 else "INSOMNIA"))

