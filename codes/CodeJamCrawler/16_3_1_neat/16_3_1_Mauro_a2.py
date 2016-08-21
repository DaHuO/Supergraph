from toolz import *

def read_int():
    return int(raw_input())

def read_ints():
    return [int(i) for i in raw_input().split()]

def solve(n, p):
    n = 0
    d = {}
    for i, v in enumerate(p):
        c = chr(ord('A') + i)
        d[c] = v
        n += v
    s = sorted([(v, k) for k, v in d.iteritems()])
    big1, big2 = s[-1][1], s[-2][1]
    r1 = ' '.join([big1 for _ in range(d[big1] - d[big2])])
    del d[big1]
    dbig2 = d[big2]
    del d[big2]
    r2 = [' '.join([k for _ in range(v)]) for k, v in d.iteritems()]
    r2 = ' '.join(r2)
    r3 = ' '.join([(big1 + big2) for _ in range(dbig2)])
    return ' '.join([r1, r2, r3])

for case in range(read_int()):
    N = read_int()
    P = read_ints()
    ans = solve(N, P).strip()
    print "Case #%d: %s" % (case+1, ans)
