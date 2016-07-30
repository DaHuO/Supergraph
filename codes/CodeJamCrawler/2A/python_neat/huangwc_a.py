import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')


def reorder(s):
    L = len(s)
    if L <= 1:
        return s
    l = reorder(s[0:L // 2])
    r = reorder(s[L // 2:])
    return l + r if l < r else r + l


for t in range(1, int(input()) + 1):

    N, R, P, S = map(int, input().split())

    result = []

    for c in 'RPS':
        D = dict(R=0, P=0, S=0)
        s = c
        D[c] = 1
        for n in range(N):
            _s = ''
            for x in s:
                if x == 'R':
                    _s += 'RS'
                    D['S'] += 1
                elif x == 'S':
                    _s += 'PS'
                    D['P'] += 1
                else:
                    _s += 'PR'
                    D['R'] += 1
            s = _s
        if P == D['P'] and R == D['R'] and S == D['S']:
            result.append(reorder(s))

    if result:
        print('Case #%s: %s' % (t, min(result)))
    else:
        print('Case #%s: %s' % (t, 'IMPOSSIBLE'))
