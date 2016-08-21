#!/c/Python27/python

import sys

def calc(n):
    if not n:
        return 'INSOMNIA'
    else:
        not_seen = set(range(10))
        i = 1
        while not_seen:
            nc = n * i
            no = nc
            d = nc % 10
            not_seen.discard(d)
            nc /= 10
            while nc:
                d = nc % 10
                not_seen.discard(d)
                nc /= 10
            i += 1
        return no


def main():
    N = int(sys.stdin.readline())
    ns = []
    for i in range(N):
        n = int(sys.stdin.readline())
        print 'Case #%d: %s' % (i + 1, calc(n))

if __name__ == '__main__':
    main()
