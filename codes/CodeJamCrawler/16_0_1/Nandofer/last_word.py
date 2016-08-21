'''
Created on Apr 15, 2016

@author: fernandomendez
'''

import argparse
import sys
import math


def solve(line):
    word = list(line)
    outword = list()
    outword = [word.pop(0)]
    for letter in word:
        if letter >= outword[0]:
            outword = [letter]+ outword
        else:
            outword.append(letter)
        
    return ''.join(outword)


parser = argparse.ArgumentParser(description='''Last word''',  epilog='')
parser.add_argument('input',  help='input file', )
parser.add_argument('output', help='output file')
args = parser.parse_args()

inFile = open (args.input)
outFile = open (args.output, 'w')
line = inFile.readline()
line= line.strip()
ncases = int(line)

for case in range(1, ncases+1):
    line = inFile.readline()
    line = line.strip()

    sol = solve(line)
    outFile.write('Case #'+str(case)+": "+str(sol)+"\n")


