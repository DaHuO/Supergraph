import sys

f = sys.stdin

T = int(f.readline())
for it in xrange(1, T + 1):
    N = int(f.readline())
    if N == 0:
        print "Case #%d: INSOMNIA" % it
    else:
        p = N
        v = set()
        while 1:
            x = str(p)
            for ch in x:
                if ch not in v:
                    v.add(ch)
            if len(v) == 10:
                break
            p += N
        print "Case #%d: %d" % (it, p)


