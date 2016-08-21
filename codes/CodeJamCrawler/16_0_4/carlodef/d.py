T = int(raw_input())
for i in xrange(T):
    K, C, S = map(int, raw_input().split())
    print "Case #%d: " % (i+1),
    for k in xrange(K):
        print k+1,
    print
