import sys

def solve(s):
    ans = ""
    for c in s:
        if ans + c < c + ans:
            ans = c + ans
        else:
            ans = ans + c
    return ans

nt = int(sys.stdin.readline())
for tc in xrange(1, nt + 1):
    s = sys.stdin.readline().strip()
    print "Case #%d:" % tc, solve(s)
    print >> sys.stderr, tc
