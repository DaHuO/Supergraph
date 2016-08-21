#!/usr/bin/env python3
# Revenge of the Pancakes

# work from bottom to the top -- don't think there's another more
# efficient method...?

# check if flipping whole stack first is better?

from sys import argv # or import sys, and use sys.argv()
# import re # for splitting with regex
# from itertools import product

# global variables and constants
inData = []
TEST = False

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

def revStack(aStack): # "reverse" in place
    newStack = aStack.replace('+','x').replace('-','+').replace('x','-')
    return newStack

def flipStack(aStack): # "flip" and "reverse"
    newStack = aStack[::-1].replace('+','x').replace('-','+').replace('x','-')
    return newStack

if TEST:
    mystack = flipStack('++++--+-+')
    print('test: ', mystack)

# problem-specific defs

# altInit()
init()            

dataset = inData.splitlines() # split on newlines
diter = iter(dataset)
T = int(next(diter))

for tt in range(1, T+1): # for each test case
    counter = 0
    stack = next(diter) # string; hmmm...
    # print("stack:", stack)
    substack = '' # this copies fine because it's a string
    
    # start at top, flip top ones to match next different one, repeat
    # check for all "-"s
    
    # be sure to reassign "stack" 
    while '-' in stack:
        counter += 1
        if stack[0] == '+':
            pivot = stack.find('-')
        else:
            pivot = stack.find('+')
        if pivot >= 0: # less than whole stack
            stack = flipStack(stack[:pivot]) + stack[pivot:]
        else:
            stack = flipStack(stack)
        
    printOutput(tt, str(counter))
    
