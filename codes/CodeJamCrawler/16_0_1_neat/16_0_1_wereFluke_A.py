T = input()
for i in xrange(1, T + 1):
    N = input()
    if N:
        j = N
        cur = []
        while True:
            #print j
            cur = cur + [int(k) for k in str(j)]
            if len(set(cur)) == 10:
                print 'Case #%d: %d' % (i, j)
                break
            j += N
    else:
        print 'Case #%d: INSOMNIA' % i
