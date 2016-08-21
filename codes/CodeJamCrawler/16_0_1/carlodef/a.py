T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    if N == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
    else:
        seen_digits = [False] * 10
        x = N
        while True:
            for d in str(x):
                seen_digits[int(d)] = True
            if all(s for s in seen_digits):
                break
            else:
                x += N
        print 'Case #%d: %d' % (i+1, x)
