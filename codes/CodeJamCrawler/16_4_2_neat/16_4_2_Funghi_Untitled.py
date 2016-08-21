T = int(input())
for case in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    PROB = list(map(float, input().split()))
    PROB.sort()
    
    MAXPROB = 0
    for i in range(0, K+1):
        PROBS = [0 for i in range(N+10)]
        PROBS[0] = 1
        for p in PROB[:i]:
            for k in range(K, 0, -1):
                PROBS[k] = PROBS[k-1] * p + PROBS[k] * (1-p)
            PROBS[0] = PROBS[0] * (1-p)
            
        for p in PROB[N-K+i:]:
            for k in range(K, 0, -1):
                PROBS[k] = PROBS[k-1] * p + PROBS[k] * (1-p)
            PROBS[0] = PROBS[0] * (1-p)

        MAXPROB = max(MAXPROB, PROBS[K//2])
        
    print("Case #%d: %.7f" % (case+1, MAXPROB))