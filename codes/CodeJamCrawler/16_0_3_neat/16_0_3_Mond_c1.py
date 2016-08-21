import itertools
from math import sqrt

T = int(raw_input().strip())


def getDivisor(n):
    step = 2 if n % 2 else 1
    for i in xrange(1, int(sqrt(sqrt(n))) + 1, step):
        if i == 1:
            continue

        if n % i == 0:
            return i

    return -1


for t in xrange(T):
    N, J = [int(k) for k in raw_input().strip().split(' ')]

    print 'Case #%d:' % (t + 1)

    cnt = 0
    for i in itertools.product('01', repeat=(N - 2)):
        s = '1%s1' % (''.join(i))
        # s = '110111'

        # print 'at %s' % s
        divisors = []
        # From base 2 to 10
        for base in xrange(2, 11):
            number = int(s, base)
            # print number
            d = getDivisor(number)
            divisors.append(d)
            # print number, d
            if d == -1:
                break

        try:
            # Try to get -1
            divisors.index(-1)
        except ValueError:
            cnt = cnt + 1

            print '%s %s' % (s, ' '.join([str(v) for v in divisors]))

            if cnt == J:
                break
