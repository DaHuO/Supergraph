t = int(raw_input())
u = 0
while u<t:
    u+=1
    n = int(raw_input())
    s = []
    d = {}
    for i in range(2*n - 1):
        s.append(map(int, raw_input().split()))
    for i in s:
        for j in i:
            try:
                d[j]+=1
            except:
                d[j]=1
    l = []
    for i in d.keys():
        if d[i]%2==1:
            l.append(i)
    l.sort()
    l = map(str, l)
    print "Case #%d: %s" %(u, ' '.join(l))
