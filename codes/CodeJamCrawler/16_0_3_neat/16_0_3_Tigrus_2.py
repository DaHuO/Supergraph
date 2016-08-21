# coding: utf-8
import sys
from random import randrange
from numpy import binary_repr

import math

def max_prime_factor(n):
    '''find the largest prime factor of integer n'''

    largest_factor = 1
    i = 2

    # i is a possible *smallest* factor of the (remaining) number n.
    # If i * i > n then n is either 1 or a prime number.
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            # Divide by the highest possible power of the found factor:
            while n % i == 0:
                n //= i
        i = 3 if i == 2 else i + 2

    if n > 1:
        # n is a prime number and therefore the largest prime factor of the 
        # original number.
        largest_factor = n
    return largest_factor

def max_divisor(n):
    return max_prime_factor(n)


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


def is_coin(n, r=10):
    b = (bytes(n))
    checked = []
    for base in range(2, r+1):
        numb = (int(b, base))
        if (is_prime(numb)):
            return False
        checked.append(numb)
    result = [max_divisor(x) for x in checked]
    return result



test_number = None
case = 0

for line in sys.stdin:
    if not test_number:
        test_number = line
        continue
    N, J = [int(x) for x in line.split(' ')]

    case += 1
    coins = set()

    n = N-1
    for x in range(2**n+1, 2**(n+1), 2):
        s = (binary_repr(x))
        r = is_coin(s)
        if r:
            r = ' '.join(map(str, r))
            coins.add("%s %s" % (str(s), r))
            if (len(coins) == J):
                break
    print('Case #%s:' % case)
    for coin in coins:
        print(coin)

