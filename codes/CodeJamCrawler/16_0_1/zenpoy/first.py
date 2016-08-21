import sys
import math


def solve(N):
    digits = set()
    if (N == 0):
        return "INSOMNIA"
    for i in xrange(1, 9 * int(10**(math.ceil(math.log10(N)) + 1)) + 1):
        K = N * i
        this_digits = set(int(x) for x in list(str(K)))
        # print digits
        digits = digits.union(this_digits)
        if (len(digits) == 10):
            return str(K)


results = []

with open(sys.argv[1]) as f:
    T = int(f.readline().rstrip())
    for i in xrange(T):
        N = int(f.readline().rstrip())
        results.append(solve(N))

for i, r in enumerate(results):
    print "Case #{0}: {1}".format(i + 1, r)
