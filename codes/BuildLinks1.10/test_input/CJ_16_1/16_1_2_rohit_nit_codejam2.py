t=input()
for i in xrange(t):
    n=input()
    a=[]
    for j in xrange(2*n - 1):
        a.append(map(int,raw_input().strip().split(' ')))
    b=[]
    c=[]
    for j in xrange((2*n)-1):
        for k in xrange(n):
            b.append(a[j][k])
    for j in xrange(len(b)):
        if b.count(b[j])%2!=0 and b[j] not in c:
            c.append(b[j])
    print "Case #%d:"%(i+1),
    c=sorted(c)
    for j in xrange(n):
        print c[j],

    print ""
