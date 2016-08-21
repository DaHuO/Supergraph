#!/usr/bin/python

t = int(raw_input())
for case_no in xrange(1, t+1):
    n = int(raw_input())
    if n == 0:
        print 'Case #%d: INSOMNIA' % (case_no, )
    else:
        a = []
        ans = n
        while True:
            for c in str(ans):
                if c not in a:
                    a.append(c)
            if len(a) == 10:
                print 'Case #%d: %d' % (case_no, ans)
                break
            ans += n
