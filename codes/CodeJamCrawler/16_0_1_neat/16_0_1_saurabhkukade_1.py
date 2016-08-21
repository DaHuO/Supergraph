xs = range(0,10)
xs = map(lambda x:str(x),xs)
xs = set(xs)

def lastNumber(n,xs,ps,m):
    for i in str(m*n):
        ps.add(i)

    #print ps,m*n
    if (len(xs)==len(ps)):
        return m*n;
    else:
        m += 1
        return lastNumber(n,xs,ps,m)


t = input()
inps = []
for i in xrange(t):
    inps.append(input())
cnt = 1
for i in xrange(t):
    ps = set()
    try:
        ans =  lastNumber(inps[i],xs,ps,1)
        print "case #"+str(cnt)+": ",ans
    except RuntimeError:
        print "case #"+str(cnt)+": INSOMNIA"
    cnt += 1
