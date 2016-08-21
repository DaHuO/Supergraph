T = int(raw_input())

for i in xrange(T):
    K, C, S = map(int, raw_input().split())
    print 'Case #' + str(i+1) + ':',
    for j in xrange(1, K):
        print j,
    print K
