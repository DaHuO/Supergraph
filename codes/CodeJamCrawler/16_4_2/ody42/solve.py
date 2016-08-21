import sys
import itertools

def prob(Ps, X, i=0):
    # Prob that X vote "yes".

    if i == len(Ps):
        return 1.0 if X == 0 else 0.0

    p = Ps[i]

    if p == 1.0:
        return prob(Ps, X-1, i+1)
    elif p == 0.0:
        return prob(Ps, X, i+1)

    return p * prob(Ps, X-1, i+1)  + (1 - p) * prob(Ps, X, i+1)

def solve(N, K, Ps):
    target = K/2
    return max(prob(r, target) for r in itertools.combinations(Ps, K))

def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        Ps = map(float, sys.stdin.readline().strip().split())
        ans = solve(N, K, Ps)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
