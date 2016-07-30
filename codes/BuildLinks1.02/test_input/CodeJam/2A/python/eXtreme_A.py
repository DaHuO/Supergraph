import sys

f = sys.stdin
# f = open("/tmp/a.in", 'r')

if f != sys.stdin:
    print 'WARNING: Input not from stdin'

def recBuild(c, n):
    if n == 0:
        return c
    if n == 1:
        if c == 'R':
            s = 'RS'
        elif c == 'P':
            s = 'PR'
        elif c == 'S':
            s = 'PS'
        return s
    else:
        base = recBuild(c, 1)
        parts = []
        for l in base:
            parts.append(recBuild(l, n-1))
        if parts[0] > parts[1]:
            parts[0], parts[1] = parts[1], parts[0]
        return parts[0] + parts[1]


tests = int(f.readline())
for t in range(1, tests+1):
    n, r, p, s = map(int, f.readline().strip().split())

    cands = []
    for c in 'RPS':
        cand = recBuild(c, n)
        d = {'R':0, 'P':0, 'S':0}

        for u in cand:
            d[u] += 1

        if d['R'] == r and d['P'] == p and d['S'] == s:
            cands.append(cand)

    cands.sort()

    if cands:
        print "Case #%d: %s" % (t, cands[0])
    else:
        print "Case #%d: IMPOSSIBLE" % t







