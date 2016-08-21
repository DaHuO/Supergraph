
import sys

def check(x):
    s = 0
    d = set()
    t = 0
    while len(d) != 10:
        s += x
        t += 1
        for ch in str(s):
            d.add(ch)

    return s

n = int(sys.stdin.readline())

for i in xrange(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print 'Case #%d: INSOMNIA' % (i + 1)
    else:
        print 'Case #%d: %d' % (i + 1, check(x))
