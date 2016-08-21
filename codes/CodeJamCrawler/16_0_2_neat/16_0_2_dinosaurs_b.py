n = input()
for i in range(1, n + 1):
    s = raw_input()
    ans = 0
    s += '+'
    for j in range(1, len(s)):
        if s[j] != s[j - 1]:
            ans += 1
    print 'Case #%d: %d' % (i, ans)
