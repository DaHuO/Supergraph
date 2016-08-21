import sys

def flips(n):
    flips = 0
    if len(n) == 0:
        return flips
    for i in xrange(1,len(n)-1):
        if n[i] != n[i-1]:
            flips += 1
    if n[:-1].endswith('-'):
        flips += 1
    return flips

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        s = f.readline()
        n = flips(s)
        print "Case #%d: %d" % (_t+1, n)
