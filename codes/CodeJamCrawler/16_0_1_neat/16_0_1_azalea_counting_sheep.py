#!/usr/bin/python


def get_number(n):
    digits = set(range(10))
    i = 0
    ub = 50000
    # after ub times, break
    while digits and ub:
        i += 1
        ub -= 1
        numbers = set(map(int, str(n * i)))
        digits -= numbers
    if digits:
        return 'INSOMNIA'
    return n * i


if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        line = f.readline().strip()
        N = int(line)
        print 'Case #%d: %s' % (i + 1, get_number(N))
