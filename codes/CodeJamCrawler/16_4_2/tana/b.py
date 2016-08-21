tt = int(raw_input())
for t in xrange(1, tt+1):
    n, k = map(int,raw_input().strip().split())
    a = map(float,raw_input().strip().split())
    a.sort()
    ans = 0.0
    for v in xrange(k+1):
        b = a[:v] + a[-(k-v):]
        y = []
        for j in xrange(n+1):
            y.append([0.0] * (n+1))
        y[0][0] = 1.0
        for i in xrange(1, k+1):
            for j in xrange(i+1):
                y[i][j] = b[i-1]*y[i-1][j-1] + (1-b[i-1])*y[i-1][j]
        ans = max(ans, y[k][k/2])
    print 'Case #%d: %f' % (t, ans)