# -*- coding: utf-8 -*-
n = int(raw_input())
for i in xrange(n):
    s = raw_input()
    ans = 1
    for j in xrange(1, len(s)):
        ans += s[j] != s[j - 1]
    if s[-1] == '+':
        ans -= 1
    print 'Case #{}: {}'.format(i + 1, ans)
