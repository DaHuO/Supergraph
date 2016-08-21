#!/usr/bin/env python3
FORMAT = "Case #{}: {}"
cases = int(input())
for i in range(cases):
    n = int(input())
    if n == 0:
        print(FORMAT.format(i + 1, "INSOMNIA"))
        continue
    seen = set()
    mul = 1
    while len(seen) != 10:
        seen |= set(str(n * mul))
        mul += 1
    print(FORMAT.format(i + 1, n * (mul - 1)))
