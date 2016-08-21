t=input();
for i in range(0,t):
    n=input();
    p=n;
    s=[];
    v=[0]*10;
    c=0;
    k=2;
    while 1==1:
        #print v
        if n in s:
            print "Case #"+str(i+1)+": INSOMNIA"
            break;
        t=n;
        s.append(n);
        while t!=0:
            r=t%10;
            if(v[r]==0):
                c=c+1;
                v[r]=1;
            t=t/10;
        if c==10:
            print "Case #"+str(i+1)+": "+str(n);
            break;
        n=p*k;
        k=k+1;
            
