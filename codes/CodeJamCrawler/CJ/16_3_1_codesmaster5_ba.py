tst=input()
for nn in range(0,tst):
    
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c=list(s)
    d={}
    for x in c:
        d[x]=0
    n=input()
    v=[]
#for i in range(0,n):
    b=raw_input()
    v=b.split(' ')
    #print v
    for mm in range(0,len(v)):
        v[mm]=int(v[mm])
    #d[c[i]]=b
    e=list(v)
    re=""
    e.sort()
    e.reverse()
    while len(e)>0:
        if e.count(e[0])%2==1:
            co=v.index(e[0])
            v[co]-=1
            re=re+ str(c[co])+' '
            e[0]=e[0]-1
            if e[0]==0:
                del e[0]
        else :
            co=v.index(e[0])
            v[co]-=1
            co1=v.index(e[1])
            v[co1]-=1
            re=re+ str(c[co])+str(c[co1])+' '
            e[0]=e[0]-1
            e[1]-=1
            if e[1]==0:
                del e[1]
            if e[0]==0:
                del e[0]
        e.sort()
        e.reverse()
    print "Case #%d: %s"%(nn+1,re)
