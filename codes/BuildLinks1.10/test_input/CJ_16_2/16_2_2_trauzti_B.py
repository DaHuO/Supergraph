import sys

def valid(q, t):
    s = str(t)
    if len(q) != len(s):
        return False
    for i in xrange(len(q)):
        if q[i] != "?" and q[i] != s[i]:
            return False
    return True

def swap(s, i, n):
    return s[:i] + str(n) + s[i+1:]

assert swap("?", 0, 9) == "9"
assert swap("0?12", 1, 9) == "0912"


def getAll(X):
    i = 0
    count = str(X).count("?")
    for x in xrange(10**count):
        s = str(X)
        div = 1
        for j in xrange(len(s)):
            if s[j] == "?":
                s = swap(s, j, (x / div) % 10)
                div *= 10
        yield s


TC = int(sys.stdin.readline())
for tc in xrange(1, 1+TC):
    C, J = sys.stdin.readline().strip().split(" ")
    diff = float("inf")
    bestC = None
    bestJ = None
    for x in getAll(C):
        for y in getAll(J):
            delta = abs(int(x) - int(y))
            if delta < diff:
                bestC = x
                bestJ = y
                diff = delta
            if delta == diff:
                if x < bestC:
                    bestC = x
                    bestJ = y
                elif x == bestC and y < bestJ:
                    bestC = x
                    bestJ = y



    s = "%s %s" % (bestC, bestJ)
    print "Case #%d: %s" % (tc, s)
