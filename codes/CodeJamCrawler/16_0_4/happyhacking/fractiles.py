import sys

def solve(N):
    maxint = sys.maxint
    seen = set()
    n = 0
    while len(seen) < 10 and maxint - n >= N :
        n += N
        k = n
        while k:
            seen.add(k % 10)
            k /= 10
    if len(seen) == 10:
        return n
    return 'INSOMNIA'


def main():
    T = int(raw_input())
    for t in range(1, T+1):
        raw = raw_input().split()
        K, C, S = int(raw[0]), int(raw[1]), int(raw[2])
        if K == S:
            res = [str(i) for i in xrange(1, K+1)]
            print 'Case #%d: %s' % (t, ' '.join(res))

if __name__ == '__main__':
    main()
