t=int(input())
z=1
while(t>0):
    n=int(input())
    if(n==0):
        print("Case #{}: INSOMNIA".format(z))
    else:
        s=set()
        j=1
        while(1):
            k=j*n
            m=k
            while(k>0):
                r=k%10
                s.add(r)
                k=int(k/10)
            j+=1
            if(len(s)==10):
                break
        print("Case #{}: {}".format(z,m))
    z+=1
    t-=1
          