import sys

def art(s, n):
    res = s
    g = "G" * len(s)
    for i in xrange(n-1):
        res = ''.join(s if c == 'L' else g for c in res)
    return res

lines = open(sys.argv[1], "rb").read().splitlines()
t = int(lines[0])
res = []

for i in xrange(1, t + 1):
    k, c, s = map(int, lines[i].split())
    res.append("Case #%d: %s\n" % (i, ' '.join(map(str, xrange(1, k+1)))))

open(sys.argv[2], "wb").write(''.join(res))
