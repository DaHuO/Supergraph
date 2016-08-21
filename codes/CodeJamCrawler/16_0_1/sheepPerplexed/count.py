import sys


def main():
    with open(sys.argv[1], 'r') as f:
        f.next()
        for idx, l in enumerate(f, start=1):
            print 'Case #{}: {}'.format(idx, count(int(l)))


def count(N):
    digits = [False] * 10
    if N == 0:
        return 'INSOMNIA'
    n = N
    while not all(digits):
        for i in str(n):
            digits[int(i)] = True
        n += N
    return n - N


if __name__ == '__main__':
    main()
