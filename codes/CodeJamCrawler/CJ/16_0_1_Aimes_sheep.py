import sys

def solve(n):
    if n == 0:
        return "INSOMNIA"

    digits = [True] * 10
    i = 0

    while any(digits):
        i += n
        n_digits = map(int, str(i))

        for digit in n_digits:
            digits[digit] = False

    return i

T = int(sys.stdin.readline())
Ns = [int(sys.stdin.readline()) for _ in xrange(T)]
i = 0

for N in Ns:
    i += 1
    print "Case #%d: %s" % (i, solve(N))
