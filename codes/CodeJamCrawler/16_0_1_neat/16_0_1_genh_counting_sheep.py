import sys


def solve(idx, b):
    if(inp == 0):
        print "Case #%d: INSOMNIA" % (idx)
        return

    a = set()
    for i in xrange(1, 1000000 + 2):
        c = b * i
        for j in list(str(c)):
            a.add(j)

        if len(a) == 10:
            print "Case #%d: %d" % (idx, c)
            break

tc = int(sys.stdin.readline())
for y in xrange(1, tc + 1):
    inp = int(sys.stdin.readline())
    solve(y, inp)
