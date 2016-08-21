from operator import mul

def sym(Q, D):
    N = len(Q)
    if N < D: return 0
    
    if D == 0: return 1
    if D == 1: return sum(Q)
    if D == N: return reduce(mul, Q, 1)
    
    mid = N/2
    ret = 0
    for d in xrange(D+1):
        ret += sym(Q[:mid], d) * sym(Q[mid:], D-d)
    return ret

def prob(Q):
    ret = 1
    K = len(Q)
    
    zero = 0
    for i in xrange(K):
        if Q[i] == 0:
            zero += 1
        else:
            ret *= Q[i]
            Q[i] = (1-Q[i])/Q[i]
    for i in xrange(K-1, -1, -1):            
        if Q[i] == 0:
            del Q[i]
    ret *= sym(Q, K/2 - zero)
    
    return ret

IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in xrange(NUM_TESTS):
    N, K = map(int,IN.readline().split())
    P = map(float,IN.readline().split())
    P.sort()
    
    answer = prob(P[:K])
    for i in xrange(K):
        answer = max(answer, prob(P[:i] + P[i-K:]))
    
    OUT.write('Case #{}: {}\n'.format(test+1, answer))
    print test+1, answer

IN.close()
OUT.close()
