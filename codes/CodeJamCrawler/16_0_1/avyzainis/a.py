#!/usr/bin/env python3

T = int(input())

for t in range(1, T + 1):
    digits = set()
    n = int(input())
    multiple = n
    if n == 0:
        print("Case #{}: INSOMNIA".format(t))
        continue

    while(len(digits) < 10):
        for digit in str(multiple):
            digits.add(digit)
        multiple += n

    print("Case #{}: {}".format(t, multiple - n))
