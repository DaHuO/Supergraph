import sys

T = int(sys.stdin.readline()[:-1])
all_digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def count(N):
    if N == 0:
        return "INSOMNIA"
    s = set()
    i = N
    while True:
        s |= set(str(i))
        if s == all_digits:
            return i
        i += N

for i in xrange(1, T+1):
    N = int(sys.stdin.readline()[:-1])
    print "Case #%d:" % i, count(N)
