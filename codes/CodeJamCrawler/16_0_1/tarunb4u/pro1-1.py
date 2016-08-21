a = [True,True,True,True,True,True,True,True,True,True]
t = int(input())
for i in range(t):
        n=int(input())
        for j,y in enumerate(a):
                a[j]=False
        count=0
        k=1
        while n!=0 and count!=10:
                m=n*k
                k+=1
                while m>0:
                        x=m%10
                        for j in range(10):
                                if x==j:
                                        a[j]=True
                        m=m/10
                count=0
                for j in range(10):
                        if a[j]:
                                count+=1
        if n==0:
                print "Case #"+str(i+1)+": INSOMNIA"
        else:
                print "Case #"+str(i+1)+": "+str(n*(k-1))