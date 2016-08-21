def solve(s):
    m = len(s)
    res = s[0]
    for i in range(1,m):
        if s[i] >= res[0]:
            res = s[i] + res
        else:
            res = res + s[i]
    return res


n = int(raw_input())
for i in range(n):
    x = raw_input()
    print 'Case #%d: %s' % (i+1, solve(x))
