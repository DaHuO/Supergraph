from sys import stdin

def best(x, level):
    if level == 0:
        return x
    if x == 'R':
        best0 = best('R', level - 1)
        best1 = best('S', level - 1)
    elif x == 'P':
        best0 = best('P', level - 1)
        best1 = best('R', level - 1)
    else:
        best0 = best('S', level - 1)
        best1 = best('P', level - 1)
    if best0 <= best1:
        return best0 + best1
    return best1 + best0

def match(s, R, P, S):
    return s.count('R') == R and s.count('P') == P and s.count('S') == S

T = int(stdin.readline())
for case in xrange(T):
    N, R, P, S = map(int, stdin.readline().split())
    bestr = best('R', N)
    bestp = best('P', N)
    bests = best('S', N)
    ans = 'IMPOSSIBLE'
    if match(bestr, R, P, S):
        ans = bestr
    elif match(bestp, R, P, S):
        ans = bestp
    elif match(bests, R, P, S):
        ans = bests
    print 'Case #{}: {}'.format(case+1, ans)
