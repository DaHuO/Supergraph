#!/usr/bin/env python3
# Senate Evacuation

from sys import argv
from time import process_time
from collections import Counter

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
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for tt in range(1, T+1): # for each test case
    # reset all parameters
    # sets must contain only immutable objects
    # tuples need trailing comma if only 1 element; ok to add comma if more than 1
    N = int(next(diter)) # number of parties
    P = [int(x) for x in (next(diter)).split()]
    PTotal = sum(P)
    evac = ''
    while PTotal > 3:
        mostCommon = P.index(max(P))
        P[mostCommon] -= 1
        evac += alphabet[mostCommon]
        mostCommon = P.index(max(P))
        P[mostCommon] -= 1
        evac += alphabet[mostCommon] + ' '
        PTotal -= 2
    if PTotal == 3:
        mostCommon = P.index(max(P))
        P[mostCommon] -= 1
        evac += alphabet[mostCommon] + ' '
        PTotal = 2
    if PTotal == 2:
        mostCommon = P.index(max(P))
        P[mostCommon] -= 1
        evac += alphabet[mostCommon]
        mostCommon = P.index(max(P))
        evac += alphabet[mostCommon]

    printOutput(tt, evac)

if TEST:
    t = process_time() - t0
    print("elapsed_time: ", t)

# printOutput(tt, str(Ni))
    
