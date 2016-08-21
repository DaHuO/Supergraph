DEBUG=0

import sys

def main():
    T = input()
    for i in range(T):
        N, K = map(int, raw_input().split())
        Pi = map(float, raw_input().split())
        print 'Case #%d: %s' % (i+1, solve(N, K, Pi))
        sys.stdout.flush()


def solve(N, K, Pi):
    Pi.sort()

    # result = 0.0
    # inds0 = range(K/2)
    # inds1 = range(N-K/2, N)
    # if DEBUG: print inds0, inds1
    # inds = inds0 + inds1
    import itertools

    # if DEBUG: print Pi
    # if DEBUG: print inds
    finalresult = 0.0
    for inds in itertools.combinations(range(N), K):
        result = 0.0
        for agree in itertools.combinations(inds, K/2):
            disagree = list(set(inds) - set(agree))
            tmp = 1.0
            for a in agree:
                tmp *= Pi[a]
            for d in disagree:
                tmp *= (1-Pi[d])
            result += tmp
            if DEBUG: print ' agree:', agree
            if DEBUG: print ' ->', tmp, result
        if result > finalresult:
            finalresult = result
    return finalresult

            
main()
