t = int(raw_input())

for cas in xrange(t):
    n = int(raw_input())
    if n == 0:
        print 'Case #{0}: INSOMNIA'.format(cas + 1)
    else:
        m = n
        s = set()
        while len(s) < 10:
            for x in str(n):
                s.add(x)
            n += m
        print 'Case #{0}: {1}'.format(cas + 1, n-m)
