def s(N, c):
    if (N==0):
        print "Case #%s:" % c, "INSOMNIA"
        return
    i = 1
    A = {}
    while len(A) < 10:
        for d in str(i*N):
            A[d] = 1
        i+=1

    print "Case #%s:" % c, (i-1)*N

T = int(raw_input())
for kk in xrange(T):
    N = int(raw_input())
    s(N, kk+1)
