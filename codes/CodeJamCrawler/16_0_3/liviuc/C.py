#!/usr/bin/python

import sys
import random
import math
import string

def base2int(ns, base):
    ret = 0
    p = 0
    for d in ns[::-1]:
        if d is '1':
            ret += math.pow(base, p)
        p += 1
    return ret

def solveDivs(nbrs):
    out = []
    for n in nbrs:
        found = False
        for div in [ 2, 3, 5, 7, 11, 13, 15, 17, 19, 23 ]:
            if n % div == 0:
                found = True
                break
        if not found:
            return None

        out.append(str(div))

    return string.join(out)

def validateCoin(jc):
    numbers = [base2int(jc, b) for b in xrange(2, 10)] + [int(jc)]
    return solveDivs(numbers)

def mkjamcoin(jlen):
    return "1{0:0{1}b}1".format(random.randint(0, math.pow(2, jlen - 2)), jlen - 2)

def solve(nfi):
    with open(nfi, 'r') as fi:
        with open(nfi.replace("in", "out"), "a") as fo:
            fo.truncate(0)
            T = int(fi.readline())
            arr = fi.readline().split()
            N = int(arr[0])
            J = int(arr[1])

            fo.write("Case #1:\n")
            found = 0
            attempts = 0
            while found < J:
                jc = mkjamcoin(N)
                divs = validateCoin(jc)
                if divs:
                    found += 1
                    fo.write("{} {}\n".format( jc, divs))
                attempts += 1

            print "Attempts: {}. Found: {}\n".format(attempts, found)

solve(sys.argv[1])
