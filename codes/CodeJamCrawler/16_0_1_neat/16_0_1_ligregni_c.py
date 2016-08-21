# Google Code Jam 2016 - Qualification Round
# Problem A

import itertools

def get_digits(x):
    return [ int(n) for n,g in itertools.groupby(str(x)) ]

def solve(x):
    s = set()
    prv = None
    cur = x
    while prv != cur and len(s) < 10:
        for e in get_digits(cur):
            s.add(e)
        prv = cur
        cur += x
    return prv if prv != cur else None

for case in xrange(int(raw_input())):
    x = int(raw_input())
    r = solve(x)
    print 'Case #%u: %s' % (case + 1, 'INSOMNIA' if not r else str(r))

