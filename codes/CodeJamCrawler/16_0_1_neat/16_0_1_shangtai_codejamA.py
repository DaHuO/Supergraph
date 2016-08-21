T = int(raw_input())
for i in xrange(T):
    N=int(raw_input())
    currentcount=[0 for tmpi in xrange(10)]
    if N==0:
        latestsheep= "INSOMNIA" 
    else:
        for j in xrange(1,10**9):
            latestsheep=str(j*N)
            for k in latestsheep:
                currentcount[int(k)]=1
            if sum(currentcount)==10:
                break
    print("Case #{}: {}".format(i+1, latestsheep))

