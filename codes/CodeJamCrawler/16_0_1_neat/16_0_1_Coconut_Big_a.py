T = int(raw_input().strip())
for t in xrange(T):
    N = int(raw_input().strip())
    if N == 0:
        print 'Case #%d: INSOMNIA' % (t + 1,)
    else:
        found = set()
        val = N
        s = '%d' % (val,)
        for x in s:
            found.add(x)
        while len(found) < 10:
            val += N
            s = '%d' % (val,)
            for x in s:
                found.add(x)
        print 'Case #%d: %d' % (t + 1, val,)
