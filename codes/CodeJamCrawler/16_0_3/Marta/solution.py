def factor(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return 1

T = input()
for i in range(T):
    N,J = map(int,raw_input().split())

    print 'Case #'+str(i+1)+": "

    # Try brute force
    count = 0
    for c in range(2**(N-2)):
        # range should be reversed for correct order but doesn't matter
        digits = [1]+[c>>x&1 for x in range(N-2)]+[1]
        factors = []
        for b in range(2,10+1):
            f = factor(reduce(lambda x,y: b*x+y, digits))
            if f == 1:
                break
            factors.append(f)
        if len(factors) == (10+1-2):
            count += 1
            print ''.join(map(str,digits)) + ' ' + ' '.join(map(str,factors))
        if count == J:
            break
