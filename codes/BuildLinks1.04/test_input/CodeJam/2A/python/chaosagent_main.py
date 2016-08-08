def dfs(r, p, s):
    total = r + p + s
    if total == 1:
        if r:
            return ['R']
        elif p:
            return ['P']
        else:
            return ['S']
    elif r > total / 2 or p > total / 2 or s > total / 2:
        return False
    i = (r + p - s) / 2
    nr = r - i
    np = i
    ns = p - i
    if nr < 0 or np < 0 or ns < 0:
        return False
    result = dfs(nr, np, ns)
    if result:
        toreturn = []
        for c in result:
            if c == 'R':
                toreturn += ['R', 'S']
            elif c == 'P':
                toreturn += ['P', 'R']
            else:
                toreturn += ['P', 'S']
        return toreturn
    else:
        return False


def sort(l, s, e):
    if e - s == 1:
        return
    m = (s + e) / 2
    sort(l, s, m)
    sort(l, m, e)
    if l[m:e] < l[s:m]:
        l[s:m], l[m:e] = l[m:e], l[s:m]

t = int(raw_input())
for case in xrange(1, t + 1):
    n, r, p, s = map(int, raw_input().split())
    result = dfs(r, p, s)
    if result:
        sort(result, 0, 2 ** n)
        print 'Case #%d: %s' % (case, ''.join(result))
    else:
        print 'Case #%d: %s' % (case, 'IMPOSSIBLE')
