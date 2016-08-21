T = int(input())

for t in range(T):
    N = int(input())
    
    if not N:
        print "Case #{0}: INSOMNIA".format(t+1)
        continue
    
    tot = set([int(i) for i in str(N)])
    k = 2
    while len(tot) != 10:
        X = k*N
        tot = tot | set([int(i) for i in str(X)])
        k = k+1
        
    print "Case #{0}: {1}".format(t+1, (k-1)*N)
        
