from sys import argv
from random import random
from math import sqrt
from itertools import count, islice

IN_FILE = argv[1]
OUT_FILE = 'out.txt'

num_tests = 0
tests = []
jamcoins = []

with open (IN_FILE, 'r') as r:
    for i, line in enumerate(r):
        if not i:
            num_tests = int(line.rstrip())
        else:
            n, j = line.rstrip().split(' ')
            tests.append((n, j))

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

def get_divisor(n):
    if is_prime(n):
        return 0
    else:
        i = 2
        while(True):
            if n % i == 0:
                return i
            i += 1

def get_divisors(n):
    divisors = []
    for i in xrange(2, 11):
        nn = int(n, i)
        divisor = get_divisor(nn)
        if divisor:
            divisors.append(str(divisor))
        else:
            return []
    return divisors

def build_random_seq(length):
    s = ''
    for i in xrange(length):
        if random() < 0.5:
            s += '0'
        else:
            s += '1'
    return s

def get_jamcoin(j_set, n):
    jamcoin = 'bypass'
    divisors = []
    while(jamcoin == 'bypass' or len(divisors) == 0):
        jamcoin = '1' + build_random_seq(n - 2) + '1'
        if jamcoin in j_set:
            jamcoin = 'bypass'
        else:
            divisors = get_divisors(jamcoin)
    res = []
    res.append(jamcoin)
    res.extend(divisors)
    return res

def get_jamcoins(test):
    n, j = test
    j = int(j)
    n = int(n)

    jamcoins_ = []
    j_set = set()
    for i in xrange (j):
        jamcoins_.append(get_jamcoin(j_set, n))
        j_set.add(jamcoins_[-1][0])
    return jamcoins_

for test in tests:
    jamcoins.append(get_jamcoins(test))

with open (OUT_FILE, 'w') as w:
    for i, jamcoin in enumerate(jamcoins):
        w.write('Case #' + str(i + 1) + ':' + '\n')
        for jamcoin_ in jamcoin:
            w.write(' '.join(jamcoin_) + '\n')
