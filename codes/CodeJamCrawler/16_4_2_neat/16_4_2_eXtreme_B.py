import sys

f = sys.stdin
#f = open("/tmp/b.in", 'r')

if f != sys.stdin:
    print 'WARNING: Input not from stdin'


def eqProb(p):
    k = len(p)
    P = [[-1.0] * (k+1) for _ in range(k+1)]

    P[0][0] = 1.0  # umowa

    for i in range(1, k+1):
        P[i][0] = P[i-1][0] * (p[i-1])
        P[0][i] = P[0][i-1] * (1.0 - p[i-1])

    def rP(y, n):
        if P[y][n] != -1.0:
            return P[y][n]

        i = y + n - 1
        v = p[i] * rP(y-1, n) + (1.0 - p[i]) * rP(y, n-1)
        P[y][n] = v
        return P[y][n]

    return rP(k/2, k/2)

tests = int(f.readline())
for t in range(1, tests+1):
    n, k = map(int, f.readline().strip().split())

    p = map(float, f.readline().strip().split())
    p.sort()

    besteqp = 0.0
    for l in range(0, k+1):
        r = n - (k - l)
        pp = p[:l] + p[r:]
        eqp = eqProb(pp)
        if besteqp < eqp:
            besteqp = eqp

    print 'Case #%d: %f' % (t, besteqp)









