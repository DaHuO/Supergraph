t=input()
f=1
for _ in range(t):
    y=input()
    p=y
    if y==0:
        print "Case #"+str(f)+": INSOMNIA"
        f+=1
        continue
    b=[0]*11
    j=2
    while(1):
        a=y
        while(a):
            x=a%10
            b[x]+=1
            a/=10
        g=0
        for i in range(0,10):
            if(b[i]):
                g+=1
        if g==10:
            break
        y=p*j
        j+=1
    print "Case #"+str(f)+": "+str(y)
    f+=1
