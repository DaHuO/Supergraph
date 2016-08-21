#!/usr/bin/env python

import numpy as np
import sys
# import os

def collectDigit(input_number):
    nDigit = len(str(input_number))
    raw = input_number
    digits = np.array([],dtype=np.int)
    for idigit in np.arange(nDigit):
        thisDigit = np.mod(raw, 10)
        digits = np.append(digits, np.array([thisDigit]))
        raw = ( raw - thisDigit ) / 10
    #print "{0}".format(digits)
    return digits

def when_to_sleep(input_number):
    nstep = 0
    digitList=np.array([],dtype=np.int)
    scan = 0
    thisNumber = input_number
    while (scan != 10) & (nstep <= 100000):
        digitList = np.unique(np.append(digitList, collectDigit(thisNumber)))
        #print digitList
        scan = len(digitList)
        thisNumber = thisNumber + input_number
        nstep += 1
    return nstep




filename = sys.argv[1]

f = open(filename)

nround = np.int(f.readline())
iround = 1
input_number_s = np.array(' '.join(f.readlines()).split()).astype(np.int)
for input_number in input_number_s:
    #print "\nDealing with {0}".format(input_number)
    step_needed = when_to_sleep(input_number)
    if step_needed > 100000:
        step_needed = 'INSOMNIA'
        print "\nCase #{0}: {1}".format(iround, 'INSOMNIA')
    else:
        print "\nCase #{0}: {1}".format(iround, step_needed * input_number)

    iround += 1