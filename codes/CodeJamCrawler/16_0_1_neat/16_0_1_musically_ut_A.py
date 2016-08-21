#!/usr/bin/env python
T = int(input())

i = 1
while i <= T:
    N = int(input())
    digit_set = set()
    if N == 0:
        print("Case #{}: INSOMNIA".format(i))
    else:
        j = 1
        while len(digit_set) < 10:
            M = j * N
            j += 1
            digit_set = digit_set.union(str(M))

        print("Case #{}: {}".format(i, M))

    i += 1

