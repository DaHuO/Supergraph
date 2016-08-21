T=int(input())
for t in range(0,T):
    N=int(input())
    if N==0:
        print("Case #%d: INSOMNIA"%(t+1))
    else:
        A = 0
        v = N
        v2=0
        p=1
        while A < 2**10 - 1:
            v2+=N
            v=v2
            while v > 0:
                v1=v%10
                v=int(v/10)
                A|=int(2**v1)
                if A>=1023:
                    break
                #print("v2=%d v1=%d v=%d A=%s"%(v2,v1,v,bin(A)))

        print("Case #%d: %d"%(t+1,v2))
