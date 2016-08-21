#!/usr/bin/env python3
# Rank and File

from sys import argv
from time import process_time

# global variables and constants
inData = []
TEST = False # not all caps

if TEST:
    t0 = process_time()
# basic IO
def init():
    if len(argv) > 0:
        # outFile = sys.argv[2]
        global inData
        with open(argv[1], "rt") as f: # should change to read filename
            inData = f.read()

def printTest(aVariable):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

if TEST:
    pass

# problem-specific defs

# main
init()
dataset = inData.splitlines()
diter = iter(dataset)
T = int(next(diter))
# print(T)

# count digits; if even number, then drop; if odd, keep

for tt in range(1,T+1):
# reset all parameters
# sets must contain only immutable objects
# tuples need trailing comma if only 1 element; ok to add comma if more than 1
# B, N = [int(x) for x in (next(diter)).split()]
    N = int(next(diter))
    # print(N)
    digits = set(next(diter).split())
    # print(digits)
    
    for ll in range(2*N-2):
        newDigits = set(next(diter).split())
        # print(newDigits)
        for dd in newDigits:
            if dd in digits:
                digits.remove(dd)
            else:
                digits.add(dd)

    intDigits = sorted([int(x) for x in digits])

    print('Case #' + str(tt) + ':', *intDigits)

# printOutput(tt, str(*list(sorted([int(x) for x in digits]))))
            
if TEST:
    t = process_time() - t0
    print("elapsed_time: ", t)
    
# printOutput(tt, str(Ni))
    
