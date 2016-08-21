#!/usr/bin/python
import sets
import sys
from math import sqrt
from itertools import count, islice

f = open(sys.argv[1], 'r')
N = int(f.readline())

def is_prime(n):
    if n < 2: return 0
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return number
    return 0

def build_pretender(num, length):
    nb = str(bin(num))[2:]
    pz = length - 2 - len(nb)
    return '1' + ('0'*pz) + str(bin(num))[2:] + '1'

def to_decimal_in_base(num, base):
    result = 0
    l = len(str(num)) - 1
    po = 0
    while l >= 0:
    	result = result + int(num[l])*(base**po)
        po = po + 1
        l = l -1
    return result


for t in range(0, N):
    nj = f.readline().split()
    n = int(nj[0])
    j = int(nj[1])
    p = 0
    results = {}
    i = 0
    divisors = []
    ps = ''
    while i != j:
        divisors = []
    	while len(divisors) != 9:
    	    divisors = []
    	    ps = build_pretender(p, n)
            if (len(ps) > n):
                p = p + 1
            	break
            #print "will try2 " + ps
    	    for base in range(2, 11):
                tdd = to_decimal_in_base(ps, base)
            	div_p = is_prime(tdd)
                #print "found " + str(div_p)
            	if (div_p != 0):
                    divisors.append(div_p)
            	else:
                    break
            p = p+1
        if len(divisors) == 9:
            #print "putting " + str(ps) + str(divisors)
	    results[ps] = divisors
            i = i + 1
    print "Case #" + str(t+1) + ":"
    for k in results:
        divisors = ' '.join(map(str, results[k]))
	print k + ' ' + divisors
