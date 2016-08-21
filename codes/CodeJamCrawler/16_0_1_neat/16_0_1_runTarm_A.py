def solve(N):
    if N == 0:
        return 'INSOMNIA'

    s = set()
    current = 0
    while len(s) < 10:
        current += N
        s.update(list(str(current)))

    return str(current)

import sys
sys.stdin = open('A-large.in', 'rt')
sys.stdout = open('A-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    N = int(raw_input().strip())
    print "Case #%d: %s" % (t, solve(N))
