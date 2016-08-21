import itertools
from random import randint
from fractions import gcd
from math import sqrt
import random

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# precompute candidate divisors
all_primes = primes(10000000)

def is_probable_prime(n):
    
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

def convert(number_string, base):

    exp = 0
    res = 0
    for e in number_string[::-1]:
        res += int(e) * (base ** exp)
        exp += 1
    return res

def yield_next_number(n=16):
    gen = itertools.product([0, 1], repeat=n)
    for e in gen:
        yield '1' + ''.join(map(str, e)) + '1'

def find_divisor(n):
    # only consider precomputed primes
    for i in all_primes:
        if n % i == 0:
            return i
    return 'NOTFOUND'

res = yield_next_number(n=30)

jam_coins = []
for candidate in res:
    print 'considering {0}'.format(candidate)
    if len(jam_coins) >= 500:
        break

    in_base_2 = convert(candidate, 2)
    in_base_4 = convert(candidate, 4)
    in_base_6 = convert(candidate, 6)
    in_base_8 = convert(candidate, 8)
    in_base_10 = convert(candidate, 10)
    if candidate.count('1') % 2 == 0 and not is_probable_prime(in_base_2) and not is_probable_prime(in_base_4) and not is_probable_prime(in_base_6) and not is_probable_prime(in_base_8) and not is_probable_prime(in_base_10):
        print 'found jam {0}'.format(candidate)

        divisors = [find_divisor(in_base_2)] + [2] + [find_divisor(in_base_4)] + [2] + [find_divisor(in_base_6)] + [2] + [find_divisor(in_base_8)] + [2] + [find_divisor(in_base_10)]
        print 'its divisors {0}'.format(divisors)
        if 'NOTFOUND' in divisors:
            continue
        jam_coins.append((candidate, divisors))

f_out = open('C_output_big_fast.txt', 'w')
f_out.write("Case #1:\n")
for jam_coin in jam_coins:
	f_out.write(jam_coin[0] + ' ' + ' '.join(map(str, jam_coin[1])) + '\n')
f_out.close()