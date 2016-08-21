T = input()
d = {0: 'A', 1: 'B', 2: 'C'}


def len2(p):
    res = ''
    r = [j for j in p if j > 0]
    ind = p.index(max(p))
    if max(r) > min(r):
        p[p.index(max(r))] = p[p.index(max(r))] + min(r) - max(r)
        res += d[ind]*(max(r) - min(r))

    al = [d[o] for o in range(len(p)) if p[o] > 0]
    r = [j for j in p if j > 0]
    if r[0] == r[1]:
        s = ' ' + str(al[0]) + str(al[1])
        res += s*r[0]

    return res


for x in range(1, T+1):
    o2 = [1, 1, 1]
    res = ''

    n = input()
    p = map(int, raw_input().split(' '))

    if len(p) == 2:
        res = len2(p)

    count = 0
    if len(p) == 3:
        while min(p) > 0:
            count += 1
            for z in range(3):
                p[z] -= o2[z]

        q = [k for k in p if k > 0]
        if len(q) == 1:
            res += d[p.index(q[0])]*q[0]

        elif len(q) == 2:
            res += len2(p)

        if count == 1:
            res += ' C AB'
        elif count == 2:
            res += ' CC AB AB'
        elif count == 3:
            res += ' CC AB AB C AB'

    print 'Case #{}: {}'.format(x, res.strip())