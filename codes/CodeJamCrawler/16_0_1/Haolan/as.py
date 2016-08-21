from sets import Set
times = int(input())
for t in range(times):
    N = int(input())
    if N == 0:
        print 'Case #'+str(t+1)+': INSOMNIA'
    else:
        m = 0
        digits = Set()
        while len(digits) < 10:
            m += 1
            n = N*m
            while n:
                digits.add(n%10)
                n /= 10
        print 'Case #'+str(t+1)+': '+str(m*N)
