a=int(input())
j=0
while j<=a:
    j+=1
    n=int(input())
    A=[0]*10
    k1=n
    u=1
    s=1
    fl=0
    while(fl!=1):
        s+=1
        if(k1==0):
            print("Case #%d: INSOMNIA" % (j))
            fl=1
            break
        k=list(set(str(k1)))
        for i in k:
            A[int(i)]=1
        if 0 in A:
            k1=(u+1)*n
            u+=1
            k=list(set(str(k1)))
        else:
            print("Case #%d: %d" % (j,k1))
            fl=1
            break
            
            
