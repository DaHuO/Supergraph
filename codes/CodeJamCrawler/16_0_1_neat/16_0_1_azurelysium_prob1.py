#!/bin/python
import sys
def rl(): return sys.stdin.readline().strip()

def sheepnum(n, multiplier=1, digits=set(), limit=10**6):
    if len(digits) == 10:
        return str(n * (multiplier-1))
    if (n > limit) or (n == 0):
        return 'INSOMNIA'
    return sheepnum(n, multiplier+1, digits.union(set(str(n*multiplier))), limit)

CASES = int(rl())
for case in xrange(CASES):
    n = int(rl())
    print 'Case #%d: %s' % (case+1, sheepnum(n))
