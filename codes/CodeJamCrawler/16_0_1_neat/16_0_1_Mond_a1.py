T = int(raw_input().strip())

for t in xrange(T):
    N = int(raw_input().strip())
    digitSet = set()
    i = 1

    if N != 0:
        while True:
            n = str(N * i)
            digitSet = digitSet.union(set(list(n)))
            if len(digitSet) == 10:
                break

            i = i + 1
    else:
        n = 'INSOMNIA'

    print 'Case #%d: %s' % (t + 1, n)
