#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import itertools as it
import pickle
import logging
import ipdb
import sys

reload(logging)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)

nums = ['ZERO', 'TWO', 'SIX', 'FOUR', 'FIVE', 'SEVEN', 'EIGHT', 'NINE', 'ONE', 'THREE']
unique = ['Z', 'W', 'X', 'U', 'F', 'V', 'G', 'I', 'O', 'T']
nums_bin = ['0', '2', '6', '4', '5', '7', '8', '9', '1', '3']

def count_char(string, char):
    amount = 0
    for char2 in string:
        if char2 == char:
            amount += 1
    return amount

def remove_num(string, number, amount):
    for char in number:
        string = remove_char(string, char, amount)
    return string

def remove_char(string, char, amount):
    num_rem = 0
    for pos, char2 in enumerate(string):
        if amount == num_rem:
            break
        if char2 == char:
            string = string[:pos-num_rem] + string[-num_rem+pos+1:]
            num_rem += 1
    return string



def solve(line):
    mystring = line
    count = np.zeros(10,dtype=int)
    for pos, num in enumerate(nums):
        char = unique[pos]
        amount = count_char(mystring, char)
        count[pos] = amount
        mystring = remove_num(mystring, num, amount)
    res = []
    for i in range(10):
        for j in range(count[i]):
            res.append(nums_bin[i])
    res.sort()
    sol = ''.join(res)
    return sol

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        line = raw_input()
        print("Case #%i: %s" % (caseNr, solve(line)))
