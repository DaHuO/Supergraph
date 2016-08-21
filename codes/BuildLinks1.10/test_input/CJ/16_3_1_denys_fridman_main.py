from string import ascii_uppercase

def solve(xs):
    N = sum(xs)
    xs = sorted(zip(xs, ascii_uppercase), reverse=True)
    xs = [[x, c] for x, c in xs]
    ans = []
    if N % 2 == 1:
        ans.append(xs[0][1])
        xs[0][0] -= 1
    while True:
        xs.sort(reverse=True)
        if xs[0][0] == 0:
            break
        s = ''
        s += xs[0][1]
        xs[0][0] -= 1
        if xs[0][0] > xs[1][0]:
            s += xs[0][1]
            xs[0][0] -= 1
        elif xs[1][0] != 0:
            s += xs[1][1]
            xs[1][0] -= 1
        ans.append(s)
    return ' '.join(ans)

for qq in xrange(1, int(raw_input()) + 1):
    N = int(raw_input())
    xs = map(int, raw_input().split())
    ans = solve(xs)
    print 'Case #%d: %s' % (qq, ans)
