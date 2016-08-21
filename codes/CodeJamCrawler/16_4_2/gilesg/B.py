import sys
from itertools import combinations

_in = open(sys.argv[1])
def raw(): return _in.readline().rstrip('\n')
def ints(): return map(int, raw().split())
def floats(): return map(float, raw().split())
raw_input = raw # we all forget sometimes

def prob(peeps, P):
    vec = []
    for sub in combinations(peeps, K/2):
        total = 1.0
        for p in peeps:
            if p in sub:
                total *= P[p]
            else:
                total *= (1-P[p])
        vec.append(total)
    vec.sort()
    return sum(vec)

def prob2(peeps, P, K):
    M = K/2
    probs = [1.0] + ([0.0]*M)
    for p in peeps:
        pr = P[p]
        for k in range(M, 0, -1):
            probs[k] = (1-pr)*probs[k] + pr*probs[k-1]
        probs[0] = (1-pr)*probs[0]
    return probs[M]

def solve(N, K, P):
    best = 0.0
    P.sort()
    for lows in range(K+1):
        his = K-lows
        best = max(best, prob2(range(lows) + range(N-his,N), P, K))

    #for peeps in combinations(range(N), K):
    #    #assert abs(prob2(peeps, P, K) - prob(peeps, P)) < 1e-6
    #    best = max(best, prob2(peeps, P, K))
    return best

if __name__ == '__main__':
    num_cases, = ints()
    for case_num in xrange(1, num_cases + 1):
        N,K = ints()
        P = floats()
        print "Case #{}: {:.9f}".format(case_num, solve(N, K, P))
