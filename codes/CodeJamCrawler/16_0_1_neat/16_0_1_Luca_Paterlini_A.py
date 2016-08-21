def get_digit(n):
    d=[0]*10
    for c in str(n): d[int(c)]=1
    return d

def test(p):
    u=1;d=[0]*10
    while sum(d)!=10:
        N = u * p
        m=get_digit(N)
        for i in xrange(10): d[i]=d[i] or m[i]
        u+=1;
        if u>10**4: return "INSOMNIA"
    return N


for i in xrange(input()):
    print "Case #%d:"%(i+1),test(input())
