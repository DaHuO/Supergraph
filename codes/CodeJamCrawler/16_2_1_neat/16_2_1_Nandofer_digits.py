'''
Created on Apr 29, 2016

@author: fernandomendez
'''

import argparse
import sys
import math


def solve(inFile):
    word = list(inFile.readline().strip())
#     print word
    word.sort()
    cl = dict()
    cl['Z'] = 0
    cl['X'] = 0
    cl['U'] = 0
    cl['W'] = 0
    cl['G'] = 0
    cl['F'] = 0
    cl['S'] = 0
    cl['H'] = 0
    cl['O'] = 0
    cl['N'] = 0
    for let in word:
        if let in ['Z' ,'X' ,'U' ,'W' ,'G' ,'F' ,'S' ,'H' ,'O' ,'N']:
            cl[let] += 1
#     print word
#     print cl
    num = list()
    for i1 in range(cl['Z']):
        num.append(0)
    for i1 in range(cl['X']):
        num.append(6)
    for i1 in range(cl['U']):
        num.append(4)
    for i1 in range(cl['W']):
        num.append(2)
    for i1 in range(cl['G']):
        num.append(8)
    for i1 in range(cl['F']-cl['U']):
        num.append(5)
    for i1 in range(cl['S']-cl['X']):
        num.append(7)
    for i1 in range(cl['H']-cl['G']):
        num.append(3)
    for i1 in range(cl['O']-cl['Z']-cl['W']-cl['U']):
        num.append(1)
    for i1 in range((cl['N']-(cl['S']-cl['X']) - (cl['O']-cl['Z']-cl['W']-cl['U']) )/2):
        num.append(9)
    num.sort()
    return ''.join([str(x) for x in num])
        


parser = argparse.ArgumentParser(description='''1A''',  epilog='')
parser.add_argument('input',  help='input file', )
parser.add_argument('output', help='output file')
args = parser.parse_args()

inFile = open (args.input)
outFile = open (args.output, 'w')
line = inFile.readline()
line= line.strip()
ncases = int(line)

for case in range(1, ncases+1):
#     print 'case ', case
    sol = solve(inFile)
    outFile.write('Case #'+str(case)+": "+str(sol)+"\n")


