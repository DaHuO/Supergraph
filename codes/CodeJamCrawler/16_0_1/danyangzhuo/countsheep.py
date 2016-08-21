t = int(raw_input())
for i in range(0,t):
    n = int(raw_input())
    if n == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
    else:
        s = set([])
        j = 1
        a = 0
        while True:
            a += n
            b = a
            while b > 0:
                s.add(b%10)
                b /= 10
            if len(s) == 10:
                print 'Case #%d: %d'% (i+1, a)
                break
