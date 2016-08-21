T = int(raw_input())
for t in xrange(T):
    k, c, s = map(int, raw_input().strip().split())
    assert k == s
    print 'Case #%d: %s' % (t + 1, ' '.join(map(str, range(1, k + 1))))
