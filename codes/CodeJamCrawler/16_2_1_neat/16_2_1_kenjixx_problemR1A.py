#!/usr/env python3
'''
Created on 2016/04/09

@author: kenji
'''
import sys
#import numpy as np

nums = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
        'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')

letters = 'NHXWOSGTZIUREVF'

def gen_problem(filename):
    with open(filename) as fsp:
        for num, line in enumerate(fsp):
            if num == 0:
                pass
            else:
                yield line.strip()


def solve_problem(numbers):
    catNum = { x : 0 for x in letters}
    for letter in numbers:
        catNum[letter] += 1

    ans = dict()
    seq = [('Z', 0), ('X', 6), ('W', 2), ('U', 4), ('R', 3),
           ('G', 8), ('S', 7), ('V', 5), ('I', 9), ('O', 1)]

    for C, tgt in seq:
        if catNum[C]:
            ans[tgt] = catNum[C]
            for v in nums[tgt]:
                catNum[v] -= ans[tgt] 

    phone_number = ''
    for y in sorted(ans.keys()):
        phone_number += str(y) * ans[y]
    return phone_number 


def solve_all(filename, ofilename):
    with open(ofilename, 'w') as ofs:
        for num, prob in enumerate(gen_problem(filename), 1):
            answer = solve_problem(prob)
            ofs.write('Case #{0}: {1}\n'.format(num, answer))


if __name__ == '__main__':
    solve_all(sys.argv[1], sys.argv[2]);