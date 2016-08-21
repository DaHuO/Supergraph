#!/usr/bin/python

import sys


def seen_all(digits_seen):
    for i in range(10):
        if digits_seen[i] == 0:
            return False
    return True


def get(N, digits_seen):
    i = 1
    while True:
        digits = [int(x) for x in str(i * N)]
        for digit in digits:
            digits_seen[digit] = 1
        if seen_all(digits_seen):
            break
        else:
            i += 1
    return i * N


def solve(i, N):
    digits_seen = [0] * 10
    if N == 0:
        times = "INSOMNIA"
    else:
        times = get(N, digits_seen)
    print "Case #{}: {}".format(i, times)


T = int(sys.stdin.readline())
for i in range(T):
    solve(i+1, int(sys.stdin.readline()))

