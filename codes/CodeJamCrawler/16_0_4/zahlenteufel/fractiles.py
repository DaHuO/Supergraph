import sys

file = sys.stdin

# file = open("in.in")

T = int(file.readline().rstrip("\n"))


def repnum(r, n, base):
    res = 0
    coef = 1
    for i in xrange(n):
        res += coef * r
        coef *= base
    return res


def eq_num(num_digits, base):
    return [repnum(digit, num_digits, base)+1 for digit in xrange(base)]


for t in xrange(1, T+1):
    K, C, S = map(int, file.readline().rstrip("\n").split(" "))
    # assume K = S
    assert K == S
    print "Case #%d:" % t, " ".join(map(str, eq_num(C, K)))
