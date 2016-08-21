T = int(raw_input().strip())


for i in xrange(T):
    S = raw_input().strip()
    ans = []

    for s in S:
        pattern = '%s%s'
        s1 = pattern % (''.join(ans), s)
        s2 = pattern % (s, ''.join(ans))
        _sorted = sorted([s1, s2])

        if _sorted[1] == s1:
            ans.append(s)
        else:
            ans.insert(0, s)

    ans = ''.join(ans)
    print 'Case #%d: %s' % (i + 1, ans)
