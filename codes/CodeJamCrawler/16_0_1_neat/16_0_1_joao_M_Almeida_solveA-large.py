def probAsolve(N):
    if N == 0:
        return -1
    digits = set()
    i = 1
    while len(digits)!=10:
        R = N * i
        r = R
        while r!=0:
            digits.add(r%10)
            r = r/10
        i+=1
    return R

with open("A-large.in") as f:
    T = int(f.next())
    for i in xrange(T):
        N = int(f.next())
        R = probAsolve(N)
        if R==-1:
            print "Case #%d: INSOMNIA" % (i+1)
        else:
            print "Case #%d: %d" % (i+1,R)
