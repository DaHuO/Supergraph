#!/usr/bin/env python3
# Counting Sheep

from sys import argv # or import sys, and use sys.argv()
# import re # for splitting with regex
# from itertools import product

# global variables and constants
inData = []
TEST = False # not all caps

# basic components for I/O and testing

# probably better coding style
def altInit():
    global inData
    try:
        with open(argv[1], 'r') as f:
            inData = f.read()
    except OSError:
        # 'File not found' error message.
        print("Fichier non trouvé")

def init():
    if len(argv) > 0:
        # outFile = sys.argv[2]
        global inData
        with open(argv[1], "rt") as f: # should change to read filename
            inData = f.read()

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

if TEST:
    pass

# problem-specific defs

# altInit()
init()            

dataset = inData.splitlines() # split on newlines
diter = iter(dataset)
T = int(next(diter))

for tt in range(1, T+1): # for each test case
    digits = set('0123456789') # 0 to 9
    counter = 0
    digitsN = set()
    N = int(next(diter)) # int
    Ni = 0
    
    if N == 0:
        printOutput(tt, 'INSOMNIA')
    else:
        while len(digits) > 0:
            Ni += N
            digitsN = set(str(Ni))
            digits -= digitsN
            # print(digitsN, digits)
        printOutput(tt, str(Ni))
    
