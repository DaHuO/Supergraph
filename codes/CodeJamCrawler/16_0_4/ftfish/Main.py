

Tn = input()
for Tc in xrange(1, Tn + 1):
    K,C,S = map(int, raw_input().split())

    print 'Case #%d:' % Tc,
    print ' '.join(map(str, xrange(1, K + 1)))

