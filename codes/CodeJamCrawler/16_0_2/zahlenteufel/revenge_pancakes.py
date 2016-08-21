import sys

file = sys.stdin

# file = open("in.in")

def unique(s):
    if not s:
        return s
    res = s[0]
    for i in xrange(1, len(s)):
        if s[i] != s[i-1]:
            res += s[i]
    return res


def min_moves(pancakes):
    return len(unique(pancakes.rstrip("+")))


T = int(file.readline().rstrip("\n"))

for i in xrange(1, T+1):
    pancakes = file.readline().rstrip("\n")
    # print pancakes, min_moves(pancakes)
    print "Case #%d: %d" % (i, min_moves(pancakes))
