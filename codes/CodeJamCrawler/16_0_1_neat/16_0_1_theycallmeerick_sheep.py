def countN(t):
    a = set()

    i = 0
    n = -1
    while len(a) < 10 and i < 100:
        n = (i + 1) * t
        for x in str(n):
            a.add(x)
        i += 1

    if i == 100 and len(a) < 10:
        return -1
    return n

n = int(raw_input().strip())

for _ in xrange(n):
    t = int(raw_input().strip())

    ret = countN(t)
    if ret == -1:
        print 'Case #%d: INSOMNIA' % (_ + 1)
    else:
        print 'Case #%d: %d' % (_ + 1, ret)
