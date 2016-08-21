#!/usr/bin/env python

__author__ = 'Bill'

from misc import input_, output_


def is_prime(n):
    """(is_prime):
        function to test if prime
        :param n: the number to test
    """
    sqr = int(n**0.5)
    if (n == 2 or n == 3):
        prime = True
    i=2
    while i <= sqr:
        if (n%i == 0):
            prime = False
            divisor = i
            i += 1
            break
        else:
            divisor = None
            i += 1
            prime = True

    return prime, divisor


def is_jamcoin(n,a):
    """(is_jamcoin):
        function to test if n is a jamcoin
        :param n: the proposed jamcoin
        :param a: length of jamcoin
    """

    divisors = []
    bases = []
    isjam = True
    isprime = False
    i = 2
    while i <= 9 and isprime == False:
        length = a - 1
        base = 0
        for ch in n:
            if ch == '1':
                base += i**length
            length -= 1
        bases.append(base)
        isprime, divisor = is_prime(base)
        divisors.append(divisor)
        i += 1
    if (isprime == True): isjam = False
    isprime, divisor = is_prime(long(n))
    if (isprime == True): isjam = False
    divisors.append(divisor)


    return isjam, divisors, bases

num_cases, cases = input_('C-small-attempt1.in')

jamcoins = []
goal = int(cases[0].split(' ')[1])

for i in xrange(16383):
    inner = format(i, 'b')
    inner = str(inner)
    test_coin = '1' + inner.zfill(int(cases[0].split(' ')[0]) - 2) + '1'
    isjam, divisors, bases = is_jamcoin(test_coin, int(cases[0].split(' ')[0]))
    if (isjam == True):
        jamcoins.append([test_coin, divisors])
        goal -= 1
        if goal == 0:
            break


output_(jamcoins, 'Coin_jam_small.out')


