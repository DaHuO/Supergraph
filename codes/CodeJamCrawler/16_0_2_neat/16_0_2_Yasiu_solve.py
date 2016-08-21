#!/usr/bin/env python3

T = int(input())
for t in range(T):
    S = input()
    n_flip = 0 if S[-1] == "+" else 1
    prev = S[-1]
    for cake in S[-2::-1]:
        if cake != prev:
            n_flip += 1
            prev = cake
    print("Case #{0}: {1}".format(t+1, n_flip))
