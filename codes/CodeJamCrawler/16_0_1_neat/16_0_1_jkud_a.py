#!/usr/bin/env python


def digits(x):
    return set(str(x))


def solve(N):
    if N == 0:
        return 'INSOMNIA'
    seen_digits = set()
    i = 0
    while len(seen_digits) < 10:
        i += 1
        seen_digits = seen_digits | digits(i*N)
    return i*N


T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    print 'Case #%d: %s' % (t+1, solve(N))
