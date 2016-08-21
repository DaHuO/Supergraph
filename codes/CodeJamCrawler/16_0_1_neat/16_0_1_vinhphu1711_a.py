T = int(raw_input())

for t in range(T):
    N0 = int(raw_input())
    if N0 == 0:
        res = 'INSOMNIA'
    else:    
        D = set()

        i = 0
        while len(D) < 10:
            i += 1
            N = N0 * i
            while N > 0:
                d = N % 10
                D.add(d)
                N = N / 10

        res = N0 * i
    print 'Case #%d: %s' % (t+1, res)