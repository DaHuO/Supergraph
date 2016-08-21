from itertools import combinations

def solve(N, K, P):
    """ solve the problem """

    _max = 0.0
    cur = []
    for _P in combinations(P, K):
        n = list(range(K))
        s = 0.0
        for V in combinations(n, int(K/2)):
            a = 1.0
            for i, p in enumerate(_P):
                if i in V:
                    a *= p
                else:
                    a *= (1-p)
            s += a
        if s > _max:
            cur = _P
        _max = max(s, _max)

    return '%.8f' % _max


def parse():
    """ parse input """

    N, K = [int(x) for x in input().split()]
    P = [float(x) for x in input().split()]

    return N, K, P


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
