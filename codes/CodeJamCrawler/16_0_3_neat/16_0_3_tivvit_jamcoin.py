import math
import itertools
tests = int(raw_input())


def smallest_divisor(i):
    d = 2
    while d <= math.ceil(math.sqrt(i)):
        r = i % d
        if r == 0:
            return d
        d += r
    return False


def base(num, base):
    c = 0
    for i, b in enumerate(reversed(num)):
        # print base ** i, b
        if b == '1':
            c += base ** i
    return c


for test in xrange(1, tests + 1):
    n, j = [int(s) for s in raw_input().split(" ")]

    print "Case #{}:".format(test)

    for i in itertools.product("10", repeat=n-2):
        coin_jam = '1' + ''.join(i) + '1'
        # print coin_jam
        divs = []
        for b in range(2, 11):
            n = base(coin_jam, b)
            d = smallest_divisor(n)
            # print b, coin_jam, n
            if not d:
                break
            divs.append(d)
        if len(divs) == 9:
            print coin_jam + ' ' + ' '.join(map(str, divs))
            j -= 1
        if not j:
            break
