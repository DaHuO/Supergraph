t = int(raw_input())

for i in xrange(1, t + 1):
    k, c, s = map(int, raw_input().split(' '))
    print "Case #%d: %s" % (i, ' '.join(map(str, range(1, k + 1))))
