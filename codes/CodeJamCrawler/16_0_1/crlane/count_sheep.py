import sys

TEST_FILENAME = 'test_data.in'

def get_digits(n):
    if n == 0:
        yield 0
    while n > 0:
        yield n % 10
        n /= 10


def solve(n):
    seen_num = set()
    seen_digits = set()
    i = 1
    orig = n
    while n not in seen_num:
        seen_num.add(n)
        seen_digits |= set(get_digits(n))
        if len(seen_digits) == 10:
            return n
        i += 1
        n = orig * i
    return 'INSOMNIA'


def read_input_and_solve(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if not i:
                T = int(line.strip())
            else:
                N = int(line.strip())
                print 'Case #{}: {}'.format(i, solve(N))


if __name__ == '__main__':
     if len(sys.argv) > 1:
         f = sys.argv[1]
     else:
         f = TEST_FILENAME
     read_input_and_solve(f)
