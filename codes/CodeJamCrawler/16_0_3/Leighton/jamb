#!/usr/bin/env python
# William Leighton Dawson
# Google Code Jam Qualification Round
# Problem 3: Coin Jam
# 2016-04-09

import sys, threading

from sympy.ntheory import isprime
from sympy.ntheory import factorint

response = []

def testcoin(jamcoin=''):
    if jamcoin == '':
        jamcoin = threading.current_thread().getName()
    global response
    sys.stderr.write("Testing " + jamcoin + '...\n')
    r = [False, []]
    bases = range(2, 11)
    for base in bases:
        c = int(jamcoin, base)
        if isprime(c):
            return r
        else:
            f = factorint(c).keys()[0]
        r[1].append(str(f))
    response.append(jamcoin + ' ' + ' '.join(r[1]))
    sys.stderr.write("Found jamcoin: " + jamcoin + ". " + str(len(response)) + " found...\n")
    r[0] = True
    return r

def nextcoin(jamcoin):
    middle = jamcoin[1:-1]
    buf = str(len(middle))
    val = int(middle, 2) + 1
    middle = format(val, '0' + buf + 'b')
    return '1' + middle + '1'

def jam(n, j):
    global response
    coin = '1' + '0'*(n-2) + '1'
    tests = []
    for i in range(j*3):
        test = threading.Thread(name=coin, target=testcoin)
        tests.append(test)
        test.start()
        coin = nextcoin(coin)
    for test in tests:
        if len(response) < j:
            test.join()
    return response[:j]

# Input as per spec. (with a few conveniences added :P)
if len(sys.argv) == 2:
    filename = sys.argv[-1]
else:
    filename = raw_input("Filename: ")
file = open(filename, 'r')
nums = [line.strip("\n").split(' ') for line in file]
file.close()
t = int("".join(nums.pop(0)))

# Output as per spec.
for i in range(t):
    num = nums[i]
    n = int(num[0])
    j = int(num[1])
    out = jam(n, j)
    print "Case #%s: %s" % (i + 1, out)

sys.stderr.write("Done!\n")
