import itertools
import math
from itertools import count, islice


def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2

    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x

    return False

def calc_base(b):
    b_values = []
    for x in range(2,11):
        v = int(b, x)
        p = get_next_prime_factor(v)
        if p:
            b_values.append(str(p))
        else:
            return

    return b_values


def get_jamcoins(n, j, count):
    b = ['1%s1' % i for i in [''.join(x) for x in [list(x) for x in list(itertools.product(['0', '1'], repeat=n-2))]]]
    print b
    jamcoins = []
    for item in b:
        if len(jamcoins) < j:
            items = calc_base(item)
            if items:
                jamcoins.append({
                    'bit': item,
                    'binarys': items
                })

    print 'Case #%s:' % count
    for coin in jamcoins:
        print coin['bit'] + ' ' + ' '.join(coin['binarys'])


fo = open("C-small-attempt4.in", "rw+")
line = fo.readlines()
lines = [x.split('\n')[0] for x in line]
lines.pop(0)

count = 0
for case in lines:
    count += 1
    params = case.split(' ')
    get_jamcoins(int(params[0]), int(params[1]), count)
