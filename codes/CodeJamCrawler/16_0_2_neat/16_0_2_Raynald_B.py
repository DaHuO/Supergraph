import sys

f = sys.stdin

T = int(f.readline())
for it in xrange(1, T + 1):
    S = f.readline().strip()
    cc = S[0]
    change = 0
    for i in xrange(1, len(S)):
        if S[i] != cc:
            change += 1
            cc = S[i]
    if S[-1] == '-':
        change += 1
    print "Case #%d: %d" % (it, change)


