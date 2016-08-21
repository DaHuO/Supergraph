#!/usr/bin/env python
from collections import defaultdict
import sys

T = int(sys.stdin.readline())

DIGITS = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
          'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')

def freq(S):
    f = defaultdict(lambda: 0)
    for c in S:
        f[c] += 1

    return f

def match_digit(s, digit):
    s = s.copy()
    for c in digit:
        if s[c] > 0:
            s[c] -= 1
        else:
            return None

    return s

def find_digits(S, digits=[]):
    if all(x == 0 for x in S.values()):
        return digits

    for d, digit in enumerate(DIGITS):
        s = match_digit(S, digit)
        if s is not None:
            found = find_digits(s, digits + [d])
            if found is not None:
                return found

    return None

for t in range(T):
    S = freq(sys.stdin.readline().strip())
    n = ''.join(map(str, sorted(find_digits(S))))
    print('Case #%d: %s' % (t + 1, n))
