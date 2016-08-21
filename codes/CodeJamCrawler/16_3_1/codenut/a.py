def to_ch(n):
    return chr(n + ord('A'))

def solve(n, p):
    r = []
    p = [[v, i] for i, v in enumerate(p)]
    cur_sum = lambda p: sum(v[0] for v in p)

    while len(p) > 0:
        p = sorted(p)[::-1]

        if p[-1][0] <= 0:
            del p[-1]
            continue

        if len(p) > 1:
            r.append(to_ch(p[0][1]) + to_ch(p[1][1]))
            p[1][0] -= 1
        else:
            r.append(to_ch(p[0][1]))

        p[0][0] -=1

    if len(r[-1]) == 1:
        r[-2], r[-1] = r[-1], r[-2]

    return r
for cas in xrange(int(raw_input())):
    n = int(raw_input())
    p = map(int, raw_input().split(' '))
    print 'Case #%d: ' % (cas + 1),
    print ' '.join(solve(n, p))
    
