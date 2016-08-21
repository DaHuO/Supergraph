t = int(raw_input())
for i in xrange(1, t + 1):
    res = []
    s = raw_input()
    res.append(s[0])
    for j in xrange(1, len(s)):
        if s[j] >= res[0]:
            res.insert(0, s[j])
        else:
            res.append(s[j])
    print "Case #{}: {}".format(i, ''.join(res))
