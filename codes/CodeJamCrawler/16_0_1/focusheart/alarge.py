def d2a(d):
    ds = "%s" % d
    a = []
    for i in range(len(ds)):
        a.append(int(ds[i]))
    a.reverse()
    return a

def a2s(a):
    a.reverse()
    a = map(str,a)
    return ''.join(a)

def rmds(a, ds):
    for i in a:
        if i in ds: ds.remove(i)
    return ds

def plus(a, b):
    lb = len(b)
    # plus each digital
    for i in range(lb):
        # part 1: < 10
        p1 = (a[i] + b[i]) % 10
        # part 2: > 10
        p2 = (a[i] + b[i]) / 10
        # change value of a[i]
        a[i] = p1
        # change value of a[i+1]
        if p2 != 0:
            if i+1 < len(a): a[i+1] = a[i+1] + p2
            else           : a.append(p2)
    # sort a
    la = len(a)
    for i in range(la):
        if a[i] > 9:
            p1 = a[i] % 10
            p2 = a[i] / 10
            a[i] = p1
            if i+1 < len(a): a[i+1] = a[i+1] + p2
            else           : a.append(p2)
    return a

def countsheep(n):
    if n==0: return 'INSOMNIA'
    oa = d2a(n)
    a = d2a(n)
    ds = [0,1,2,3,4,5,6,7,8,9]
    while(True):
        ds = rmds(a, ds)
        if ds == []: break
        a = plus(a, oa)
    return a2s(a)

def test():
    for i in range(10**5,10**6):
        a = countsheep(i)
        print i, a

def dbg(msg):
    #print msg
    pass

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        n = int(s)
        a = countsheep(n)
        print "Case #{}: {}".format(i, a)

if __name__=='__main__':
    main()
