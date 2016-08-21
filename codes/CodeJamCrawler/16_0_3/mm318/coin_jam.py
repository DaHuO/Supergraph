import os, sys, inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if not(cmd_folder in sys.path):
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], 'libs')))
if not(cmd_subfolder in sys.path):
    sys.path.insert(0, cmd_subfolder)


import math
import random
import itertools
from collections import defaultdict
import subprocess


def Tree():
    return defaultdict(Tree)


primes = []

def gen_primes(max_num):
    num = 2
    while(num <= max_num):
        limit = int(math.sqrt(num)) + 1
        is_prime = True
        for prime in primes:
            if(prime > limit):
                break
            if(num % prime == 0):
                is_prime = False
                break
        if(is_prime):
            primes.append(num)
            # print num
        num += 1


def is_probable_prime(n, k = 7):
    """use Rabin-Miller algorithm to return True (n is probably prime) or False (n is definitely composite)"""
    if n < 6:           # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:    # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        # Use random.randint(2, n-2) for very large numbers
        for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in xrange(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


def to_decimal(string, radix_base):
    num = 0
    base = 1
    for i in range(len(string)):
        if(string[-i-1] == '1'):
            num += base
        base *= radix_base
    return num


def main(args):
    in_file_path = args[1]
    in_file = open(in_file_path, 'rb')
    
    # print is_probable_prime(3333333333333333)
    # print is_probable_prime(11111111111111111111111111110111)
    # print is_probable_prime(982451653)

    # gen_primes(3333333333333333)
    gen_primes(999999)
    # print primes

    # print to_decimal('110111', 3)
    # print to_decimal('110111', 10)

    T = int(in_file.readline())
    for i in range(T):
        NJ = in_file.readline().split()
        N = int(NJ[0])
        J = int(NJ[1])

        # print 'Case #%d: %d %d' % (i+1, N, J)
        print 'Case #%d:' % (i+1)

        num_jamcoins_found = 0
        for s in itertools.product('01', repeat=N-2):
            coin_str = '1' + ''.join(s) + '1'
            # sys.stdout.write(coin_str)
            divisors = []
            for i in range(2, 11):
                num = to_decimal(coin_str, i)
                # sys.stdout.write(' ' + str(num))
                if not(is_probable_prime(num)):
                    # sys.stdout.write('*')
                    limit = int(math.sqrt(num)) + 1
                    for prime in primes:
                        if(prime > limit):
                            break
                        if(num % prime == 0):
                            divisors.append(str(prime))
                            break
            # sys.stdout.write('\n')
            # print divisors
            if(len(divisors) >= 9):
                print coin_str, ' '.join(divisors)
                num_jamcoins_found += 1
            if(num_jamcoins_found >= J):
                break

    return 0


if(__name__ == "__main__"):
    ret = main(sys.argv)
    sys.exit(ret)

