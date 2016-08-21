#!/usr/bin/env python

import sys
import os

digits = set()
for i in range(10):
    digits.add(i)

def getDigits(number):
    result = set()
    strNum = str(number)
    for i in range(len(strNum)):
        result.add(int(strNum[i]))
    return result

def getLastNumber(number):
    count = set()
    idx = 1
    while count != digits:
        count.update(getDigits(idx * number)) 
        idx += 1
    return (idx-1)*number

lines = open(sys.argv[1]).readlines()
cases = int(lines[0])
for i in range(cases):
    number = int(lines[i+1])
    if number == 0:
        print("Case #%s: INSOMNIA" % (i+1))
    else:
        print("Case #%s: %s" % (i+1, getLastNumber(number)))

