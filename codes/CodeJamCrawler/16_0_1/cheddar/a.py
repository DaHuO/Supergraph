#!/usr/bin/env python

for cas in xrange(input()):
    N=input()
    if N==0:
        ans = 'INSOMNIA'
    else:
        cur=N
        seen = set()
        while True:
            seen.update(list(str(cur)))
            if len(seen)==10:
                break
            cur += N
        ans = str(cur)
    print "Case #%d: %s" % (cas+1, ans)
