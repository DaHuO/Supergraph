#!/usr/bin/env python3
import sys


def counting(n):
    if n == 0:
        return "INSOMNIA"

    digits = set()
    remaining = 10
    m = n
    i = 1
    while True:
        if m >= sys.maxsize:
            return "INSOMNIA"
        init_m = m
        while m > 0:
            digit = m % 10
            if digit not in digits:
                digits.add(digit)
                remaining -= 1
                if remaining == 0:
                    return init_m
            m = int(m / 10)
        i += 1
        m = n * i

t = int(input())
for i in range(1, t+1):
    n = int(input())
    r = counting(n)
    print("Case #{}: {}".format(i, r))
