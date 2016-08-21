#!/usr/bin/env python3

T= int(input())
for t in range(T):
    N = int(input())
    seen = set()

    if N == 0:
        print("Case #{}: INSOMNIA".format(t+1))
    else:
        i = 1
        base = N
        while len(seen) <= 9:
            for c in str(N):
                seen.add(c)
            if len(seen) == 10:
                break
            i += 1
            N = base * i
        print("Case #{0}: {1}".format(t+1, N))
