import sys

T = int(sys.stdin.readline().strip())

for it in xrange(T):
    k, c, s = map(int, sys.stdin.readline().strip().split())
    print "Case #%d:" % (it + 1), " ".join(map(lambda x: str(1 + x * k ** (c - 1)), xrange(k)))