import sys


def count(n):
    digits = set(range(10))
    i = 10 * 1000
    x = n
    while len(digits) > 0 and i > 0:
        last_number = x
        digits -= set([int(c) for c in str(x)])
        x += n
        i -= 1

    if len(digits) == 0:
        return last_number
    else:
        return 'INSOMNIA'


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline().strip())
        for t in range(T):
            n = int(f.readline().strip())
            print "Case #%d: %s" % (t + 1, str(count(n)))
