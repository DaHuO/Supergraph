t = int(raw_input())

for i in xrange(t):
    s = raw_input()


    tmp = ''
    for l in (s):
        if (l + tmp > tmp + l):
            tmp = l + tmp
        else:
            tmp = tmp + l

    print 'Case #%d: %s' % (i + 1, tmp)