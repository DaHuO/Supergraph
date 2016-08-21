
T = int(raw_input())

for t in range(T):
    res = []
    s = raw_input()
    K, C, S = s.split()
    K = int(K)
    C = int(C)
    S = int(S)
     
    if (K != S): 
        print("Case #{0}: IMPOSSIBLE".format(t+1))
    else:
        print("Case #{0}: {1}".format(t+1, ' '.join([str(i+1) for i in range(K)])))
