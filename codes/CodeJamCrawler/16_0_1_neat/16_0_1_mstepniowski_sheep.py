import sys


MAX_N = 10**6


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    numbers = line.strip().split()
    return [int(n) for n in numbers]


def solve(n):
    c = 0
    digits = set()
    for i in range(MAX_N):
        c += n
        digits.update(str(c))
        # print c, digits
        if len(digits) == 10:
            return i, c
    return None, 'INSOMNIA'


def max_tries():
    result = 0
    for n in range(555555, MAX_N + 1):
        i, _ = solve(n)
        if i is None:
            print "didn't find max for %d" % n
        result = max(i, result)
        if n % 1000 == 0:
            print "%d: %d iterations, %d max " % (n, i, result)
    return result


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        n = read_numbers()
        print "Case #%d: %s" % (t + 1, solve(n[0])[1])
