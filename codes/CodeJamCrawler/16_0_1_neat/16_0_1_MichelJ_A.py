import sys
import StringIO

def doit(N):
    nN = N
    sN = str(nN)
    dN = set(sN)
    maxi = 10000
    i = 0
    while len(dN) < 10 and i < maxi:
        nN += N
        sN = str(nN)
        dN |= set(sN)
        i += 1
    if i >= maxi:
        return "INSOMNIA"
    return sN

sample = """5
0
1
2
11
1692
"""

def main(data = None):
    if data is None:
        f = sys.stdin
    else:
        f = StringIO.StringIO(data)
    nt = int(f.readline())
    for tc in xrange(nt):
        N = int(f.readline())
        print "Case #%d: %s" % (tc+1, doit(N))

main()
