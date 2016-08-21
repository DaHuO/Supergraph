def read_int():
    return int(raw_input())


def check(num, d):
    while num > 0:
        digit = num % 10
        if digit in d:
            del d[digit]
        num = num / 10


def solve():
    N = read_int()
    d = dict((x, 0) for x in range(0, 10))
    if N == 0:
        return 'INSOMNIA'
    i = 1
    while len(d) > 0:
        val = N * i
        check(val, d)
        if len(d) == 0:
            return val
        i += 1


def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
    main()
