import sys

def solve(n, p, r, s):
    mx = max(p, r, s)
    mn = min(p, r, s)
    if n == 1:
        if p == 0:
            return "RS"
        elif r == 0:
            return "PS"
        else:
            return "PR"
    if n % 2 == 0:
        if p == mx:
            return solve(n - 1, p / 2, p / 2, p / 2 - 1) + solve(n - 1, p / 2, p / 2 - 1, p / 2)
        elif r == mx:
            return solve(n - 1, r / 2, r / 2, r / 2 - 1) + solve(n - 1, r / 2 - 1, r / 2, r / 2)
        else:
            return solve(n - 1, s / 2, s / 2 - 1, s / 2) + solve(n - 1, s / 2 - 1, s / 2, s / 2)
    else:
        q = mn / 2
        if s == mn:
            return solve(n - 1, q + 1, q, q) + solve(n - 1, q, q + 1, q)
        elif r == mn:
            return solve(n - 1, q + 1, q, q) + solve(n - 1, q, q, q + 1)
        else:
            return solve(n - 1, q, q + 1, q) + solve(n - 1, q, q, q + 1)


tc = int(sys.stdin.readline())
for t in xrange(1, tc + 1):
    n, r, p, s = map(int, sys.stdin.readline().split())
    if max(r, p, s) != min(r, p, s) + 1:
        print "Case #%d: IMPOSSIBLE" % t
    else:
        print "Case #%d: %s" % (t, solve(n, p, r, s))
