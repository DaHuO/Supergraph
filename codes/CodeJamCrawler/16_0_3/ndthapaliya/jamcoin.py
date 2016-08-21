import math
import random
import sys

def is_prime_quick_fail(n, threshold=10000):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    if math.sqrt(n) > threshold:
        for i in range(3, threshold, 2):
            if n % i == 0:
                return False
        # too long, don't care
        return True
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def first_divisor(n):
    assert n > 1
    if n % 2 == 0:
        return 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i


def divisors(jamcoin):
    return list(map(first_divisor, convert_to_bases(jamcoin)))


def is_jamcoin(jamcoin):
    for n in convert_to_bases(jamcoin):
        if is_prime_quick_fail(n):
            return False
    return True


def convert_to_bases(jamcoin):
    assert type(jamcoin) is str
    assert jamcoin[0] == jamcoin[-1] == '1'

    return [int(jamcoin, i) for i in range(2, 11)]


def random_string_gen(length):
    l = ['1'] + [''] * (length - 2) + ['1']
    for i in range(1, length - 1):
        l[i] = random.choice(['1', '0'])
    return ''.join(l)


def pp(s):
    print('%s %s' % (s, ' '.join(str(i) for i in divisors(s))))


if __name__ == '__main__':
    n, j = (int(i) for i in sys.argv[1:])

    out_set = set()

    while len(out_set) < j:
        s = random_string_gen(n)
        if is_jamcoin(s):
            out_set.add(s)


    print('Case #1:')
    for s in out_set:
        pp(s)
