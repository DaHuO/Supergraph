import fileinput
from collections import defaultdict


def solve(inp):
    h = defaultdict(int)
    for line in inp:
        for c in line.split(' '):
            h[c] += 1
    ret = []
    for k, v in h.iteritems():
        if v%2 != 0:
            ret.append(int(k))
    return ' '.join(map(str, sorted(ret)))


reader = enumerate(fileinput.input())
reader.next()
i = 0
for _, line in reader:
    i += 1
    N = int(line.strip())
    arr = []
    for j in xrange(2*N-1):
        _, line = reader.next()
        arr.append(line.strip())
    res = solve(arr)
    print "Case #%d: %s" % (i, res)
