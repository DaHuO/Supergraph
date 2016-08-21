for cas in xrange(1, 1 + input()):
    k, c, s = map(int, raw_input().strip().split())
    str = '1'
    for i in range(2, k+1):
        str += " {}".format(i)
    print "Case #%s: %s" % (cas, str)
