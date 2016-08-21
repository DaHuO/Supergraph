from collections import defaultdict



def solve(mat, N):
    d = defaultdict(int)
    for row in mat:
        for col in row:
            d[col] += 1
    res = []
    for n, cnt in d.items():
        if cnt % 2 == 1:
            res.append(n)
    res.sort()
    return res


for qq in xrange(1, int(raw_input()) + 1):
    N = int(raw_input())
    rows = []
    for _ in xrange(2*N-1):
        rows.append(map(int, raw_input().split()))
    ans = solve(rows, N)
    ans = ' '.join(map(str, ans))
    print 'Case #%d: %s' % (qq, ans)
