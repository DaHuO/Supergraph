


f=open("A-large.in",'r')
g=int(f.readline())
r=1
for d in range(g):
    ac=f.readline()[:-1]
    a=ac[1:]
    if len(a)==0:
        print "Case #"+str(r)+": "+str(ac)
    else:
        k=ac[0]
        for i in a:
            if i>=k[0]:
                k=i+k
            else:
                k=k+i
        print "Case #"+str(r)+": "+k
    
    r=r+1
