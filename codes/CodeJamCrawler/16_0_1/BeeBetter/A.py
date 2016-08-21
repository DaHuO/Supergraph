for cas in xrange(1, 1 + input()):
    n = input()
    if n == 0:
        print "Case #%s: INSOMNIA" % (cas)
        continue
    i = 0
    a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    k = 0
    while i < 1000 and len(a) > 0:
        k = k + n
        m = k
        while m > 0:
            a.discard(m % 10)
            m = m / 10
        i = i + 1
    if i == 1000:
        print "Case #%s: INSOMNIA" % (cas)
        bf = True
        continue
    print "Case #%s: %s" % (cas, k)