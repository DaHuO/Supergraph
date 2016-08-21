t=input()
for r in range(t):
    n=input()
    a=[]
    i=1
    if n==0:
        print "Case #"+str(r+1)+": INSOMNIA"
    else :
        for j in range(10):
            a.append(0)
        while(True):
            k=n*i
            while(k>0):
                m=k%10
                if a[m]==0:
                    a[m]=1
                k=k/10
            if(a.count(1)==10):
                break
            i=i+1
        print "Case #"+str(r+1)+": "+str(n*i)
