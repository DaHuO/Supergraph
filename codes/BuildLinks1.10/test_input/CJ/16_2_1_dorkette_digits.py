#!/usr/bin/env python3
# Getting the Digits

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

digits = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6,
          'SEVEN':7, 'EIGHT':8, 'NINE':9}

# ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE
# unique letters: Z0, W2, U4, X6, G8  

# ONETHREEFIVESEVENNINE
# unique letters: F5, H3, O1, R3, S7, T3

# print(digits['THREE'])

digitOrder = ['ZERO', 'TWO', 'FOUR', 'SIX', 'EIGHT', 'ONE', 'THREE', 'FIVE', 'SEVEN']
letterOrder = ['Z', 'W', 'U', 'X', 'G', 'O', 'H', 'F', 'S']
numberOrder = ['0', '2', '4', '6', '8', '1', '3', '5', '7', '9']

for tt in range(1, T+1): # for each test case
    # reset all parameters
    # sets must contain only immutable objects
    # tuples need trailing comma if only 1 element; ok to add comma if more than 1
    phone = []
    allNumbers = next(diter)
    allCount = Counter(allNumbers)
    # print(allCount)
    for ll in range(len(letterOrder)):
        lc = allCount[letterOrder[ll]]
        # print(ll, letterOrder[ll], allCount[letterOrder[ll]])
        if lc > 0:
            phone.append(numberOrder[ll]*lc)
            letters = Counter(digitOrder[ll])
            for cc in range(lc):
                allCount.subtract(letters)
    phone.append('9'*allCount['I'])
    phone = ''.join(sorted(phone))
    printOutput(tt, phone)

if TEST:
    t = process_time() - t0
    print("elapsed_time: ", t)

# printOutput(tt, str(Ni))
    
