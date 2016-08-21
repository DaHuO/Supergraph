


T = int(raw_input())

for i in xrange(T):
    K, C, S = [int(x) for x in raw_input().split()]

    res = ' '.join([str(j) for j in xrange(1, K + 1)])

    print 'Case #%d: %s' % (i + 1, res)
