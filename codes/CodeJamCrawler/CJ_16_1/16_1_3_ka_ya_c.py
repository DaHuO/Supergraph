def solve(n, fs):
    fs = [f-1 for f in fs]
    lp = [None for p in xrange(n)]
    for i in xrange(n):
        chk = [False for p in xrange(n)]
        p = i
        cnt = 0
        while not chk[p] and not lp[p]:
            chk[p] = True
            p = fs[p]
            cnt += 1
        if p == i:
            while not lp[p]:
                lp[p] = (cnt, 0)
                p = fs[p]
    for i in xrange(n):
            p = i
            cnt = 0
            while not lp[p]:
                p = fs[p]
                cnt += 1
            l, b = lp[p]
            if cnt > b:
                lp[p] = (l, cnt)
    res = 0
    tmp = 0
    for i in xrange(n):
        if lp[i]:
            l, b = lp[i]
            if l == 2:
                j = fs[i]
                _, bj = lp[j]
                tmp += l + b + bj
            else:
                if l > res:
                    res = l
    if tmp / 2 > res:
        res = tmp / 2
    return res


T = input()
for i in xrange(1, T+1):
    N = input()
    Fs = map(int, raw_input().split())
    print 'Case #{}: {}'.format(i, solve(N, Fs))
