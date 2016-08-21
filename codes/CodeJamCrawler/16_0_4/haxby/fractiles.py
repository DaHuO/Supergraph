
def fractiles(K, C, S):
    if K==1 and S>=1 and C>1:
        return "1"
    elif S==K-1 and C>1:
        return " ".join([str(i) for i in range(2,K+1)])
    elif S>=K:
        return " ".join([str(i) for i in range(1,K+1)])
    else:
        return "IMPOSSIBLE"
    

    
n = int(raw_input())
for i in range(n):
    K, C, S  = map(int, raw_input().split())
    check = fractiles(K,C,S)
    print "Case #{0}: {1}".format(i+1, check)
    
