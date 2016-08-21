'''
Created on Apr 15, 2016

@author: fernandomendez
'''

import argparse
import sys
import math


def solve(inFile):
    includ_vls= dict()
    missing_vals=list()
    line = inFile.readline().strip()
    nlet =int(line)
    for lin in range(2*nlet-1):
        line = inFile.readline().strip()
        vals = [int(x) for x in line.split() ]
        for va in vals:
            if va not in includ_vls:
                includ_vls[va] = 1
            else:
                includ_vls[va] += 1
    keys = includ_vls.keys()
    print keys
    print includ_vls
    for key in includ_vls:
        if includ_vls[key]%2 ==1:
            missing_vals.append(key)
    missing_vals.sort()
    return ' '.join(str(x) for x in missing_vals)


parser = argparse.ArgumentParser(description='''Template''',  epilog='')
parser.add_argument('input',  help='input file', )
parser.add_argument('output', help='output file')
args = parser.parse_args()

inFile = open (args.input)
outFile = open (args.output, 'w')
line = inFile.readline()
line= line.strip()
ncases = int(line)

for case in range(1, ncases+1):
    sol = solve(inFile)
    outFile.write('Case #'+str(case)+": "+str(sol)+"\n")


