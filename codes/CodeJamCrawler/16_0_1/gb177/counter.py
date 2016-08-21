#!/usr/bin/python

def N(): return tuple(map(int, raw_input().split()))

digits = set("0123456789")

#
# small
#
def solve(n):
    if n == 0:
        return -1

    m = n
    seen = set(str(n))
    while seen != digits:
        m += n
        seen |= set(str(m))
    return m

T = N()[0]
for c in range(T):
    n = N()[0]
    s = solve(n)
    if s == -1:
        s = "INSOMNIA"
    else:
        s = str(s)
    print "Case #%d: %s" % (c+1, s)

