import itertools as it

def calc_prob(P):
    '''
    If P[i] is the probability of an event A[i], return the probability
    that exactly k of these events occured, for any k
    '''
    A = [1-P[0], P[0]]
    for i in xrange(1,len(P)):
        newA = [0]*(i+2)
        newA[0] = A[0] * (1-P[i])
        newA[i+1] = A[i] * P[i]
        for j in xrange(1, i+1):
            newA[j] = A[j] * (1-P[i]) + A[j-1] * P[i]
        A = newA

    return A

def slow_ans(P, K):
    return max(calc_prob(Q)[K/2] for Q in it.combinations(P,K))
        
T = int(raw_input())
for t in xrange(1, T+1):
    N, K = map(int, raw_input().split())
    P = map(float, raw_input().split())
    print "Case #%d: %f"%(t, slow_ans(P,K))
