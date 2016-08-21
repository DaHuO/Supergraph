T = input()
for test_case in xrange(T):
    s = raw_input()
    tmp = ''
    pre = '*'
    for j in xrange(len(s)):
        if s[j] != pre:
            pre = s[j]
            tmp = tmp + s[j]
    print 'Case #%d: %d' % (test_case + 1, len(tmp) + (tmp[-1] == '-') - 1)

