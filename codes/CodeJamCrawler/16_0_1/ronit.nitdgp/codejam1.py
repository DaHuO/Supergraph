t=input()
for i in xrange(t):
    n=input()
    if n==0:
        print "Case #%d:"%(i + 1),"INSOMNIA"
        continue
    a=[]
    for k in xrange(10):
        a.append(0)
    j=1
    x=1
    while(x!=0):
        y=j*n
        flag=0
        while(y!=0):
            r=y%10
            y=y/10
            a[r]=1
        for k in xrange(10):
            if(a[k]==0): flag=1
        if flag==0:
            print "Case #%d:"%(i + 1),j*n
            x=0
        j+=1
    del a