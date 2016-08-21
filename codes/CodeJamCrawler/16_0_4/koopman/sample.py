import sys

inf = sys.argv[1]

"""
starts = ["LLL", "LLG", "LGL", "LGG", "GLL", "GLG", "GGL", "GGG"]
for start in starts:
    s = start
    for i in xrange(1, 3):
        new_s = ""
        for c in s:
            if c == "L":
                new_s += "LGL"
            else:
                new_s += "GGG"
        s = new_s
    print start, s

exit()
"""

f = open(inf, 'rU')
outf = open(inf + ".out", 'w')

T = int(f.readline())
for t in xrange(T):
    (T, C, S) = [int(x) for x in f.readline().split()]
    print T, C, S
    if S > T:
        outf.write("Case #{0}: IMPOSSIBLE\n".format(t+1))

    """
    n = T * 3 * (C-1)
    div = n / S
    tiles = []
    for i in xrange(S):
        tiles.append( 1 + i * div )
    """
    outf.write("Case #{0}: {1}\n".format(t+1, " ".join((str(x+1) for x in xrange(S)))))


f.close()
outf.close()
