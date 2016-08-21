
def tobase(L, K):
    r = 0
    for l in L:
        r = r*K+l
    return r
def solve(K, C, S):
    if K == 1: return '1'
    if S*C < K: return 'IMPOSSIBLE'
    S = (K + C - 1) // C
    t = range(K)
    return ' '.join(str(1+tobase(t[C*i:C*(i+1)], K)) for i in range(S))