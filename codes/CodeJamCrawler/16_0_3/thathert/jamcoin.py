# -*- coding: utf-8 -*-

"""\

┻┻︵⁞=༎ຶ﹏༎ຶ=⁞︵┻┻


"""

from __future__ import print_function

import argparse


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def readl(f):
    return f.next().strip()


def is_probably_prime(n):
    return pow(2, n - 1, n) == 1


def verify_jamcoin(c, primes=set()):
    for base in range(2, 11):
        n = int(c, base)
        if is_probably_prime(n):
            return False
    return True


def divisors(c, primes=[]):
    divs = []
    for base in xrange(2, 11):
        n = int(c, base)
        for i in primes:
            if n % i == 0:
                divs.append(i)
                break
    return divs


def process(coin_length, num_coins, primes=set()):
    inner_length = coin_length - 2
    results = []
    found = 0
    for x in xrange(int('1' * inner_length, 2) + 1):
        coin = bin(x).split('b')[1].zfill(inner_length).join(['1'] * 2)
        print(coin)
        if verify_jamcoin(coin, primes=primes):
            results.append((coin, divisors(coin, primes=primes)))
            found += 1
            print('Found %s: %s' % (found, coin))
            if found >= num_coins:
                break
    return results


def output_results(results, f):
    for i, res in enumerate(results):
        print('Case #%s:' % (i + 1), file=f)
        for coin, divs in res:
            print(' '.join([coin] + map(str, divs)), file=f)


def solve(f, primes=set()):
    test_cases = readl(f)
    results = []
    try:
        while True:
            n = readl(f)
            results.append(process(*map(int, n.split(' ')), primes=primes))
    except StopIteration:
        pass
    return results


def load_primes(n):
    primes = []
    for prime in gen_primes():
        primes.append(prime)
        if prime > n:
            break
    return primes


def main():
    # TODO: fix positional args
    parser = argparse.ArgumentParser(description='The prices are mixed!')
    parser.add_argument('file', type=str, help='the input', default='./data/in')
    parser.add_argument('output', type=str, help='the output', default='./data/out')
    args = parser.parse_args()
    primes = load_primes(33333333)
    print('primes')
    with open(args.file) as f:
        x = solve(f, primes=primes)
    with open(args.output, 'w') as f:
        output_results(x, f)


if __name__ == '__main__':
    main()

