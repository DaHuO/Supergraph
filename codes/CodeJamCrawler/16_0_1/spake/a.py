#!/usr/bin/env python2.7

t = int(raw_input())

for i in xrange(t):
    num_digits_seen = 0
    digits_seen = [False]*10

    n = int(raw_input())
    if n == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
    else:
        cnt = 0
        m = n

        while True:
            for digit in str(m):
                digit = int(digit)
                if not digits_seen[digit]:
                    digits_seen[digit] = True
                    num_digits_seen += 1

            if num_digits_seen == 10:
                print 'Case #%d: %d' % (i+1, m)
                break

            cnt += 1
            m = n * cnt
