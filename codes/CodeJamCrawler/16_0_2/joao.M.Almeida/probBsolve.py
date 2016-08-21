def probBsolve(S):
    c = S[0]
    flip=0
    for i in xrange(len(S)):
        if(S[i]!=c):
            c =S[i]
            flip+=1
    if(c=='-'):
        flip+=1
    return flip

with open("probBtest.in") as f:
    T = int(f.next())
    for i in xrange(T):
        N = f.next()
        N=N[:-1]
        R = probBsolve(N)
        print "Case #%d: %d" % (i+1,R)
