#!/usr/bin/env python

T = input()
for t in xrange(T):
    n = input()

    app = {}
    for i in xrange(2 * n - 1):
        nums = map(int, raw_input().split())
        for num in nums:
            if num not in app:
                app[num] = 0
            app[num] += 1

    res = []
    for num in app:
        if app[num] % 2 == 1:
            res.append(num)
    res.sort()

    print 'Case #%d: %s' % (t + 1, ' '.join(map(str, res)))
