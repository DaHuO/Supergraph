import math

def positions_to_ind(K, chain):
    tmp = 1
    for i, c in enumerate(reversed(chain)):
        assert 1 <= c <= K
        tmp += (K**i) * (c - 1)
    return tmp

def solve_D(K, C, S):
    if K > C * S:
        return "IMPOSSIBLE"

    def clipped_range(K, beg, end):
        r = []
        for i in range(beg, end):
            if i < 1:
                r.append(1)
            elif i > K:
                r.apend(K)
            else:
                r.append(i)
        return r

    inds = []
    for i in xrange(K / C):
        r = range(i*C+1, (i+1)*C+1)
        inds.append(positions_to_ind(K, r))

    if K % C != 0:
        r = clipped_range(K, K+1-C, K+1)
        inds.append(positions_to_ind(K, r))
    return ' '.join(map(str, inds))

def main_D():
    T = input()
    for i in range(T):
        K, C, S = map(int, raw_input().split())
        print 'Case #%d: %s' % (i+1, solve_D(K, C, S))


if __name__ == '__main__':
    main_D()
