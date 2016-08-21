#!/usr/bin/env python

import math, random, sys

CUTOFF = 500

def get_divisor(n):
    if n <= 3:
        return 0
    for i in xrange(2,int(math.floor(math.sqrt(n)))+1):
        if i > CUTOFF:
            return 0
        if n % i == 0:
            return i
    return 0

def random_str(length):
    n = random.randint(0, 2**length-1)
    return "{0:b}".format(n).zfill(length)

def helper(N, J):
    jamcoins = []
    #for i in xrange(2**(N-2)):
    str_tried = set()
    while True:
        #n_str = '1' + "{0:b}".format(i).zfill(N-2) + '1'
        n_str = '1' + random_str(N-2) + '1'
        if n_str in str_tried:
            continue
        str_tried.add(n_str)
        divs = []
        is_jamcoin = True
        for base in xrange(2,11):
	    n_base = int(n_str, base)
    	    div = get_divisor(n_base)
	    if div <= 1 or div >= n_base:
	        is_jamcoin = False
	        break
	    divs.append(div)
        if is_jamcoin:
	    jamcoins.append([n_str] + divs)
        if len(jamcoins) == J:
            break

    return jamcoins

def parse_file(num_lines=-1):
    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    i = 1
    tests = []
    varying_nlines = False
    if num_lines == -1:
        varying_nlines = True

    while i < len(lines):
        new_test = []
        if varying_nlines:
            num_lines = int(lines[i])
            i += 1

        for j in range(num_lines):
            new_test.append(lines[i])
            i += 1
        tests.append(new_test)
    return int(lines[0]), tests

num_tests, tests = parse_file(num_lines=1)
#num_tests, tests = parse_file()

for case,test in enumerate(tests):
    N, J = [int(x) for x in test[0].split()]
    sol = helper(N, J)
    print 'Case #1:'
    for s in sol:
        print ' '.join([str(x) for x in s])
