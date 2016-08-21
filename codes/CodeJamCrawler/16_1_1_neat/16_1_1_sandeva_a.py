import sys

def f(S):
    r, S = S[0], S[1:]
    while S:
        s, S = S[0], S[1:]
        r = s + r if s >= r[0] else r + s
    return r


with open(sys.argv[1]) as fi:
    for i, n in enumerate(fi.readlines()[1:]):
        print "Case #%d:" % (i + 1), f(n.strip())
