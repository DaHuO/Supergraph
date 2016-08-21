T = int(raw_input())
for t in xrange(T):
    K, C, S = map(int, raw_input().split())
    gap=K**(C-1)
    print "Case #"+str(t+1)+": ",
    for s in xrange(S):
        print s*gap+1,
    print
    