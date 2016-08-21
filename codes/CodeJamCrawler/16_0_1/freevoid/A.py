import sys

INSOMNIA = 'INSOMNIA'

def get_digits(n):
    return map(int, str(n))

def solve(n):
    if n == 0:
        return INSOMNIA

    digits = set(get_digits(n))

    if len(digits) == 10:
        return n

    i = 2
    while True:
        new_n = i * n
        digits.update(get_digits(new_n))
        if (len(digits) == 10):
            return new_n
        i += 1


def read_int(fp):
    return int(fp.readline())

if __name__ == '__main__':
    T = read_int(sys.stdin)
    for i in range(T):
        print 'Case #%d: %s' % (i + 1, solve(read_int(sys.stdin)))
