test_cases = int(raw_input())

for case in xrange(1, test_cases + 1):
    t, k, c = [int(i) for i in raw_input().split()]

    u = []
    for i in xrange(0, t):
        a = ['L'] * t
        a[i] = 'G'
        b = ''.join(a)
        for j in xrange(1, k):
            s = ''
            for e in b:
                if e == 'G':
                    s += 'G'*t
                else:
                    s += ''.join(a)
            b = s[:t]
        u.append(b)
    l = set()
    for i in xrange(0, len(u)):
        for j in xrange(0, t):
            if u[i][j] == 'G':
                l.add(j + 1)

    l = [str(i) for i in l]
    if len(l) > c:
        l = []
        l.append('IMPOSSIBLE')
    print "Case #{}: {}".format(case, ' '.join(l))
