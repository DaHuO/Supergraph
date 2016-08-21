t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    n = input()
    hs = [0]*10
    if(n==0):
        print "INSOMNIA"
    else:
        x = 0
        while(0 in hs):
            x+=1
            N=str(n*x)
            for i in N:
                hs[int(i)]=1
        print N
            
            
