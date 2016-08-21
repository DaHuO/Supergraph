import sys

f = sys.stdin

T = int(f.readline())
for it in xrange(1, T + 1):
    K, C, S = map(int, f.readline().strip().split(' '))
    if S < K:
        print "Case #%d: IMPOSSIBLE" % it
    else:
        se = []
        for x in xrange(1, S + 1):
            se += [str(x)]
        print "Case #%d:" % it, ' '.join(se)
