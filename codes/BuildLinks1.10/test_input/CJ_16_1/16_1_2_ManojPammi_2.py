f=open("B-large.in",'r')
g=int(f.readline())
for d in range(g):
    a=int(f.readline()[:-1])
    g={}
    for i in range(2*a-1):
        m=f.readline()[:-1]
        t=m.split()
        for l in t:
            if l in g:
                g[l]=g[l]+1
            else:
                g[l]=1
    c=[]
    for h in g:
        if (g[h]%2)!=0:
            c.append(int(h))
    rt=sorted(c)
    y=[]
    for v in rt:
        y.append(str(v))
    print "Case #"+str(d+1)+": "+" ".join(y)
    
