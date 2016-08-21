#!/usr/bin/env python3
from collections import Counter


def split(N):
    if N == 0:
        yield 0
    while N:
        yield N % 10
        N //= 10

t = int(input())
for case in range(1, t + 1):
    N = int(input())
    digits = Counter()
    i = 1
    result = N
    while len(digits.keys()) < 10:
        result = N * i
        digits.update(split(result))
        i += 1
        if N * i == N * (i - 1):
            result = "INSOMNIA"
            break
    print("Case #{}: {}".format(case, result))
