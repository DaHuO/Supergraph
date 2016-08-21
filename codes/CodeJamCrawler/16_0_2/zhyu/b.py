t = int(raw_input())

for cas in xrange(t):
    s = raw_input().strip()
    cnt = 0
    ok = (s[0] == '+')
    now = s[0]
    for x in s[1:]:
        if x == now:
            continue
        cnt += 1
        ok = (x == '+')
        now = x
    if not ok:
        cnt += 1
    print 'Case #{0}: {1}'.format(cas + 1, cnt)
