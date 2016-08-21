T = int(raw_input())

def sol1(N):
    seen = set()
    t = N
    for i in xrange(1, 10000):
        seen = seen.union(set(str(t)))
        if len(seen) == 10:
            return t
        t += N
    return 'INSOMNIA'

for i in xrange(1, T + 1):
    print 'Case #%s: %s' % (i, sol1(int(raw_input())))