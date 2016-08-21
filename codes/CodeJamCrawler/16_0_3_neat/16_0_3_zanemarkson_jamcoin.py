#!/usr/bin/env python

import numpy as np
import sys

def getDivisors(candidate):
    divisors = -1
    wall=np.floor(np.sqrt(candidate)).astype(np.int)
    for trial in np.arange(2, wall+1):
        if (np.mod(candidate, trial) == 0):
            divisors = trial
    return divisors

def interprete(binary_string, base_number):
    return int(binary_string, base_number)

def checkCoin(binary_string):
    divisors = np.array([],dtype=np.int)
    for base_number in np.arange(2,11):
        thisNumberBaseTen = interprete(binary_string, base_number)
        thisDivisor = getDivisors(thisNumberBaseTen)
        if (thisDivisor == -1):
            return False, np.array([],dtype=int)
        else:
            divisors = np.append(divisors, [thisDivisor])
    return True, divisors

# Main Function ...



filename = sys.argv[1]
f = open(filename)
nround = np.int(f.readline())
line = np.array(f.readline().split(), dtype=int)

N = line[0]
n = N - 2
J = line[1]

rawStart = 0
rawStop = 2 ** n - 1


print "Case #1:"
count = 0
for rawNumber in np.arange(rawStart, rawStop+1):
    thisNumber = (2**(N-1)) + (2 * rawNumber) + 1
    if (count < J):
        binary_string = bin(thisNumber)[2:]
        isJamCoin, goodDivisor = checkCoin(binary_string)
        if (isJamCoin):
            print('{}\t'+'{}\t'*len(goodDivisor)).format(binary_string, *goodDivisor)
            count += 1
    elif (count >= J):
        break


