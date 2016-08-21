T = input()
for t in xrange(1, T+1):
    N = input()
    if N == 0:
        print 'Case #%d: INSOMNIA' % t
        continue
    result = N
    digits = set(str(result))
    while len(digits) < 10:
        result += N
        digits |= set(str(result))
    print 'Case #%d: %d' % (t, result)
