import sys
import StringIO


def doit(K, C, S):
    if S==K:
        return " ".join(map(str, range(1, S+1)))
    return "IMPOSSIBLE"

sample = """5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3
"""

def stripnl(s):
    if s[-1]=="\n":
        return s[:-1]
    return s

def main(data = None):
    if data is None:
        f = sys.stdin
    else:
        f = StringIO.StringIO(data)
    nt = int(f.readline())
    for tc in xrange(nt):
        inp = stripnl(f.readline())
        K, C, S = map(int, inp.split(" "))
        print "Case #%d: %s" % (tc+1, doit(K, C, S))

main()
