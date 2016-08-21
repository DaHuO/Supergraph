def solve(S):
    n = 0
    p = None
    for s in S:
        if s == '-' and p != '-':
            n += 2 if p == '+' else 1
        p = s
    return n

import sys
sys.stdin = open('B-large.in', 'rt')
sys.stdout = open('B-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    S = raw_input().strip()
    print "Case #%d: %d" % (t, solve(S))
