# -*- coding: utf-8 -*-
"""
A jamcoin is a string of N ≥ 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
Not every string of 0s and 1s is a jamcoin. For example, 101 is not a jamcoin; its interpretation in base 2 is 5, which is prime. But the string 1001 is a jamcoin: in bases 2 through 10, its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001, respectively, and none of those is prime.

We hear that there may be communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. (A nontrivial divisor for a positive integer K is some positive integer other than 1 or K that evenly divides K.) For convenience, these divisors must be expressed in base 10.

For example, for the jamcoin 1001 mentioned above, a possible set of nontrivial divisors for the base 2 through 10 interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.

Can you produce J different jamcoins of length N, along with proof that they are legitimate?
"""
import fileinput
import math
import random
import string
import sys

random.seed('tobi')

bases = (2,3,4,5,6,7,8,9,10)
jamcoins_used = set()


def random_coin(length):
    l = random.getrandbits(length - 2)
    bitstring = str(bin(l))[2:]
    bitstring = bitstring.ljust(length - 2, '0')
    return '1{}1'.format(bitstring)


def is_maybe_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for _ in range(2):
        a = random.randrange(2, num)
        if pow(a, num - 1, num) == 1:
            return True
    return False


def find_divisor(num):
    if num <= 3:
        return None
    if is_maybe_prime(num):
        return None

    i = 2
    while i * i <= 1000:  # we are lazy
        if num % i == 0:
            return i
        i += 1
    return None


def test_coin(coin):
    """returns divisors for each base if coin is a jamcoin; otherwise None"""
    divisors = []
    for base in bases:
        representation = string.atoi(coin, base)
        sys.stdout.flush()
        divisor = find_divisor(representation)
        if divisor:
            divisors.append(divisor)
        else:
            return None
    return divisors


def get_jamcoin(length):
    while True:
        coin = random_coin(length)
        if coin in jamcoins_used:
            continue
        jamcoins_used.add(coin)

        divisors = test_coin(coin)
        if divisors:
            return coin, divisors


for i, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        num_cases = int(line)
    else:
        N, J = line.split()
        N = int(N)
        J = int(J)
        print 'Case #{0}:'.format(i)
        for _ in range(J):
            jamcoin, divisors = get_jamcoin(N)
            divisors = ' '.join(str(i) for i in divisors)
            print '{} {}'.format(jamcoin, divisors)
            sys.stdout.flush()