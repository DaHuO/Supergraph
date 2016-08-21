import sys

with open(sys.argv[1]) as f:
    ls = [x.strip() for x in f.readlines()]
    for i in xrange(1, len(ls)):
        l = ls[i]
        lc = l[0]
        flips = 0 if l[-1] == '+' else 1
        for c in l[1:]:
            if c != lc:
                lc = c
                flips += 1
        print 'Case #%d: %d' % (i, flips)
