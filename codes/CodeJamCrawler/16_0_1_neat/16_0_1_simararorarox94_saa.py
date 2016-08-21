t=input()
xx=1
while t>0:
    n=input()
    if n==0:
        print "Case #%d: INSOMIA" %(xx)
        t-=1
        xx+=1
        continue
    j=1
    a=[0]*10
    x=n
    while 1:
        x=n*j
        y=x
        while y>0:
            r=y%10
            a[r]=1
            y/=10
        f=0
        for i in range(0,10):
           if a[i]==0:
               f=1
        if f==0:
            break
        j+=1
    print "Case #%d: %d" %(xx,x)
    xx+=1
    t-=1
