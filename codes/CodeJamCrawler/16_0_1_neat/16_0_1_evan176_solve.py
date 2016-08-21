#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def compute(number):
    codebook = dict()
    for i in range(1, 100):
        temp = i*number
        temp = str(temp)
        for digit in temp:
            if digit not in codebook:
                codebook[digit] = 1
            if len(codebook.keys()) > 9:
                return temp 
    return 'INSOMNIA'


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        cases = f.readline()
        for i in range(int(cases)):
            number = int(f.readline())
            result = compute(number)
            print('Case #{}: {}'.format(i+1, result))
