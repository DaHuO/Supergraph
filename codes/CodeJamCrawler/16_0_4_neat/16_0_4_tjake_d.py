IMP = "IMPOSSIBLE"
for t in xrange(input()):
    print "Case #%d:" % (t+1),
    k, c, s = map(int, raw_input().split())

    # k==s case
    print ' '.join(map(str, range(1, k+1)))
