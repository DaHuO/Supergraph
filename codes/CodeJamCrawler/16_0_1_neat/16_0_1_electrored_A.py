import sys

rd = open("A-large.in","r")
wrt = open("A.out", "w")

def fun(n):
    n = list(str(n))
    n = map(int,n)
    return n

for test in xrange(1, int(rd.readline().strip()) + 1):
    n = int(rd.readline().strip())
    sf = set([0,1,2,3,4,5,6,7,8,9])
    s = set()
    f = 0
    nt = n
    for i in xrange(1000):
        n1 = n
        for nm in fun(n1):
            s.add(nm)
        if s == sf:
            ans = "Case #%d: %d\n" %(test, n)
            wrt.write(ans)
            f = 1
            break
        else:
            n += nt
    if f == 0:
        ans = "Case #%d: INSOMNIA\n" %(test)
        wrt.write(ans)
wrt.close()
