#!/usr/bin/env python3

T = int(input())

for i in range(1, T + 1):
    N = int(input())

    if N == 0:
        print("Case #%d: INSOMNIA" % i)
        continue

    x = N
    bits = 0
    while bits != (1 << 10) - 1:
        y = x
        while y > 0:
            r = y % 10
            y //= 10
            bits |= 1 << r

        x += N

    print("Case #%d: %d" % (i, x - N))
