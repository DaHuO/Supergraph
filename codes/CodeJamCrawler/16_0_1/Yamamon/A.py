T = int(raw_input())

for case in xrange(1, T+1):
    N = int(raw_input())
    result = 'INSOMNIA'
    if N != 0:
        seen = set()
        k = 1
        while len(seen) < 10:
            n = N * k
            seen = seen.union([c for c in str(n)])
            k += 1
        result = str(N * (k-1))

    print 'Case #%d: %s' % (case, result)
