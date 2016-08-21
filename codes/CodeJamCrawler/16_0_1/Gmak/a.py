t=int(input())
i=1
while(t>0):
    n=int(input())
    if(n==0):
        print("Case #{}: {}".format(i,"INSOMNIA"))
    else:
        S=set()
        j=1
        while(1):
            k=j*n
            m=k
            while(k>0):
                c=k%10
                S.add(c)
                k=int(k/10)
            j+=1
            if(len(S)==10):
                break
        print("Case #{}: {}".format(i,m))
    i+=1
    t-=1
        