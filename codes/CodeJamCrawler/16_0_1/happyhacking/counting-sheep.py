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
    for i in range(1, T+1):
        N = int(raw_input())
        if N == 0:
            print 'Case #%d: %s' % (i, 'INSOMNIA')
        else:
            res = solve(N)
            print 'Case #%d: %s' % (i, res)

if __name__ == '__main__':
    main()
