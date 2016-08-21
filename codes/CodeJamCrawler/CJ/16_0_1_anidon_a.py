t=input()

for k in range(t):
    N=input()
    if(N==0):
        print "Case #{}: INSOMNIA".format(k+1)
        continue
    
    d=dict()
    p=1
    while(1):
        list_N=list(str(N*p))
        for i in range(len(list_N)):
            d[list_N[i]]=1
        if(len(d.keys())==10):
            print "Case #{}: {}".format(k+1,N*p)
            break
        
        else:
            p=p+1
