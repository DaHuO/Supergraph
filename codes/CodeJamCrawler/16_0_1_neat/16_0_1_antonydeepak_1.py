Tc=int(input())
for t in range(1,Tc+1):
    N=int(input())
    ans="INSOMNIA"
    if(N!=0):
        acc=0
        i=1
        while(acc!=1023):
            n=i*N
            while n>0:
                acc=acc|1<<(n%10)
                n=n//10
            ans=i*N
            i+=1
    print("Case #{0}: {1}".format(t,ans))