tt = int(raw_input())
def minz(a1, a2):
    if a1 is None:
        return a2
    elif a2 is None:
        return a1
    else:
        return min(a1, a2)

for t in xrange(1, tt+1):
    n, rr, pp, ss = map(int,raw_input().strip().split())
    pow3 = [1]
    for i in xrange(1, 1<<n):
        pow3.append(pow3[i-1] * 3)
    xp = []
    xr = []
    xs = []
    for i in xrange(n+1):
        yp = []
        yr = []
        ys = []
        for j in xrange((1<<n)+1):
            yp.append([None] * ((1<<n)+1))
            yr.append([None] * ((1<<n)+1))
            ys.append([None] * ((1<<n)+1))
        xp.append(yp)
        xr.append(yr)
        xs.append(ys)
    xp[0][1][0] = 0
    xr[0][0][1] = 1
    xs[0][0][0] = 2
    for i in xrange(1, n+1):
        for j in xrange((1<<i)+1):
            for k in xrange((1<<i)+1):
                gp = None
                gr = None
                gs = None
                for j1 in xrange(j+1):
                    for k1 in xrange(k+1):
                        j2 = j-j1
                        k2 = k-k1
                        if (xp[i-1][j1][k1] is not None) and (xr[i-1][j2][k2] is not None):
                            gp = minz(gp, xp[i-1][j1][k1]*pow3[1<<(i-1)]+xr[i-1][j2][k2])
                        if (xp[i-1][j1][k1] is not None) and (xs[i-1][j2][k2] is not None):
                            gs = minz(gs, xp[i-1][j1][k1]*pow3[1<<(i-1)]+xs[i-1][j2][k2])
                        if (xr[i-1][j1][k1] is not None) and (xp[i-1][j2][k2] is not None):
                            gp = minz(gp, xr[i-1][j1][k1]*pow3[1<<(i-1)]+xp[i-1][j2][k2])
                        if (xr[i-1][j1][k1] is not None) and (xs[i-1][j2][k2] is not None):
                            gr = minz(gr, xr[i-1][j1][k1]*pow3[1<<(i-1)]+xs[i-1][j2][k2])
                        if (xs[i-1][j1][k1] is not None) and (xp[i-1][j2][k2] is not None):
                            gs = minz(gs, xs[i-1][j1][k1]*pow3[1<<(i-1)]+xp[i-1][j2][k2])
                        if (xs[i-1][j1][k1] is not None) and (xr[i-1][j2][k2] is not None):
                            gr = minz(gr, xs[i-1][j1][k1]*pow3[1<<(i-1)]+xr[i-1][j2][k2])
                xp[i][j][k] = gp
                xr[i][j][k] = gr
                xs[i][j][k] = gs
    anx = []
    if xp[n][pp][rr] is not None:
        anx.append(xp[n][pp][rr])
    if xr[n][pp][rr] is not None:
        anx.append(xr[n][pp][rr])
    if xs[n][pp][rr] is not None:
        anx.append(xs[n][pp][rr])
    if len(anx) == 0:
        ans = 'IMPOSSIBLE'
    else:
        m = min(anx)
        s = []
        for i in xrange(1<<i):
            if m % 3 == 0:
                s.append('P')
            elif m % 3 == 1:
                s.append('R')
            else:
                s.append('S')
            m /= 3
        ans = ''.join(s[::-1])
    print 'Case #%d: %s' % (t, ans)