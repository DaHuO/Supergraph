n = input()
for i in range(n):
    m = input()
    if m == 0:
        ans = 'INSOMNIA'
    else:
        cur = 0
        seen = set()
        while len(seen) < 10:
            cur += m
            for digit in str(cur):
                seen.add(digit)
        ans = str(cur)
    print 'Case #%d: %s' % (i + 1, ans)
