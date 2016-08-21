def solve():
    s = list(reversed(raw_input()))
    z = -1
    turnover = False
    while len(s) > 0:
        c = '+'
        if turnover:
            c = '-'
        while len(s) > 0 and s[0] == c:
            s = s[1:]
        z += 1
        turnover = not turnover
    return z

T = int(raw_input())
for i in range(1, T+1):
    ans = solve()
    print('Case #%d: %d' % (i, ans))
