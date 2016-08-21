#!/usr/bin/python2
import sys
import multiprocessing
import logging
import os
import itertools
import math
import gmpy2
import copy
import collections
import string
import scipy.stats as stats
import argparse

# from https://oeis.org/A000040
def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# N = 16 for small dataset, max int is 1e16 -> use 10**8
# For large, need to find only 500 jamcoins - smaller value is sufficient
listofprimes = rwh_primes(10**4)


def solve(casedata):
    """ Solve case """
    [N, J] = casedata
    valdivs = []
    numrepr = 1 << (N-2)  # excludes LSB 1
    while len(valdivs) < J:
        dividers = []
        for b in range(2, 11):
            num = 1
            numbits = numrepr
            bitnum = 0
            while numbits > 0:
                bitnum += 1
                if numbits % 2 == 1:
                    num += b**(bitnum)
                numbits >>= 1
            divider = 0
            for prime in listofprimes:
                if prime < num and num % prime == 0:
                    divider = prime
                    break
            if divider == 0:
                break
            dividers.append(divider)
        if len(dividers) == 9:
            binrepr = bin(numrepr)[2:] + "1"
            if len(binrepr) != N:
                print("Error: not enough jamcoins found")
                break
            valdivs.append((binrepr, dividers))
        numrepr += 1


    result = ''
    for val, div in valdivs:
        result += "\n%s %s" % (val, ' '.join([str(d) for d in div]))
    return result

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N, J = map(int, sys.stdin.readline().rstrip('\n').split())
        casedata = [N, J]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument('-m', '--multiprocessing', action='store_true', default=False, required=False)
    aparser.add_argument('-t', '--test-parser', action='store_true', default=False, required=False)
    args = aparser.parse_args()
    cases = parse()
    if args.test_parser:
        print(cases)
        sys.exit(1)
    if args.multiprocessing:
        p = multiprocessing.Pool(multiprocessing.cpu_count())
        resultobjs = [p.apply_async(solve, [case]) for case in cases]
        for case, resultobj in enumerate(resultobjs):
            print('Case #%d: %s' % (case + 1, resultobj.get()))
            sys.stdout.flush()
    else:
        for case, data in enumerate(cases):
            result = solve(data)
            print('Case #%d: %s' % (case + 1, result))
            #sys.stdout.flush()
        p = multiprocessing.Pool(multiprocessing.cpu_count())

    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()


    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #resultobjs = [p.apply_async(solve, [case]) for case in cases]
    #for case, resultobj in enumerate(resultobjs):
    #    print('Case #%d: %s' % (case + 1, resultobj.get()))
    #    sys.stdout.flush()
