import sys

count = int(sys.stdin.readline())


def res(N):
    i = 1
    mult = 1*N
    s = set()
    if N == 0:
        return "INSOMNIA"
    while len(s) < 10:
        mult = i * N
        for d in str(mult):
            s.add(int(d))
        i += 1
    return mult


for tc in xrange(1,count+1):
    N = int(sys.stdin.readline())
    print "Case #%d: %s" % (tc, res(N))
