#!/usr/bin/python

import sys
from multiprocessing import Process
from primes import primes  # python set of prime numbers

input_file = sys.argv[1] if len(sys.argv) > 1 else 'c_sample.in'
radixes = (2, 3, 4, 5, 6, 7, 8, 9, 10)
divisors_dict = {}

def is_prime(n):  # Modified from http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    if n in primes: return False  # Added
    r = int(n**0.5)
    f=5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def factors(n):  # Taken from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def quick_factor(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i

def build_divisiors_dict(valid_coin):
    for i in radixes:
        computed = int(valid_coin, base=i)  # Gross should have probably made a class to maintain this object
        # decent_divisor = list(factors(computed))
        # decent_divisor = decent_divisor[len(decent_divisor)/2]
        decent_divisor = quick_factor(computed)
        divisors_dict[valid_coin][str(i)] = decent_divisor


def valid(jamcoin):
    divisors_dict[jamcoin] = {}
    for i in radixes:
        computed = int(jamcoin, base=i)
        if is_prime(computed):
            return False
    return True


def generate_coins(NJ):
    digits, needed_coins = NJ.split(' ')
    valid_coins = set()
    def add_coin(possible_coin):
        if valid(possible_coin):
            valid_coins.add(possible_coin)
            add_divisors = Process(target=build_divisiors_dict(possible_coin))
            add_divisors.start()

    between_digits = int(digits) - 2
    end = int('1'*between_digits, base=2)
    for i in range(0, end+1):
        if len(valid_coins) < int(needed_coins):
            between_string = format(bin(i)[2:]).zfill(between_digits)
            possible_coin = '1' + between_string + '1'
            check_coin = Process(target=add_coin(possible_coin))
            check_coin.start()
    for coin in valid_coins:
        divisors = [divisors_dict[coin][str(radix)] for radix in radixes]
        print coin + ' ' + ' '.join([str(i) for i in divisors])


with open(input_file, 'r') as f:
    test_cases = int(f.readline())
    assert(1<=test_cases<=100)

    for test in xrange(0, test_cases):
        NJ = f.readline().rstrip('\n')
        print "Case #{}:".format(test+1)
        generate_coins(NJ)

f.close()
