from pprint import pprint
from itertools import count
import math
from random import randrange, randint

def is_prime(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def divisor_generator(n):
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n))):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def find_divisor(binary, bases):
    divisors = []
    for base in bases:
        for divisor in divisor_generator(base):
            divisors.append(divisor)
            break
    return divisors

def no_primes(binary, bases):
    for base in bases:
        if is_prime(base):
            return False
    else:
        return True

def find_bases(binary):
    return [int(binary, x) for x in (2, 3, 4, 5, 6, 7, 8, 9, 10)]

def generate_random_numbers(length):
    while True:
        x = '{0:b}'.format(2**(length - 1) + randint(0, 2**(length - 2)))
        if str(x).startswith('1') and str(x).endswith('1'):
            yield x

def generate_numbers(length):
    i = 0
    while True:
        i += 1
        x = '{0:b}'.format(2**(length - 1) + i)
        if str(x).startswith('1') and str(x).endswith('1') and len(x) == length:
            yield x

def compute(length, coins):
    numbers = possible_numbers(length)
    possible_jam_coins = find_bases(numbers)
    jam_coins= find_jam_coins(possible_jam_coins)
    results = find_divisor(jam_coins, coins)
    count = 0
    final = []
    for binary, info in results.iteritems():
        if len(info['bases']) == len(info['divisors']):
            printable = '{} {}'.format(binary, ' '.join([str(x) for x in info['divisors']]))
            final.append(printable)
            count += 1
        if count >= coins:
            break
    return final

i = 1
for test in range(int(raw_input().strip())):
    N, J = map(int, raw_input().strip().split(' '))
    print 'Case #{}:'.format(i)
    found_dict = {}
    for binary in generate_random_numbers(N):
        bases = find_bases(binary)
        if no_primes(binary, bases) and binary not in found_dict.keys():
            divisors = find_divisor(binary, bases)
            if len(divisors) == len(bases):
                found_dict[binary] = {'bases': bases, 'divisors': divisors}
        if len(found_dict.keys()) >= J:
            break
    for binary, divisors in found_dict.iteritems():
        print '{} {}'.format(binary, ' '.join([str(x) for x in found_dict[binary]['divisors']]))
    i += 1
