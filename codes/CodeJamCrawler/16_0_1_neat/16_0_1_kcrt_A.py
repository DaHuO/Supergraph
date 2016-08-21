# -*- coding: utf-8 -*-

T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        result = "INSOMNIA"
    else:
        n = 0
        digits_seen = set()
        while len(digits_seen) != 10:
            n += N
            for x in str(n):
                digits_seen.add(x)
        result = str(n)
    print("Case #" + str(t + 1) + ": " + result)
