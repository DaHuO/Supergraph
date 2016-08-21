import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'D'
input_file = None

input_file = None

def readstr():
    return next(input_file).strip()

def readintlist():
    lst = list(map(int, readstr().split()))
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def solvecase():
    K, C, S = readintlist()
    tiles_to_check = list(reversed(range(K)))
    addresses = []
    while tiles_to_check:
        power = 0
        current = 0
        while tiles_to_check:
            tile = tiles_to_check.pop()
            current += tile * K ** power
            power += 1
            if power >= C:
                break
        addresses.append(current)
    if len(addresses) > S:
        return 'IMPOSSIBLE'
    return ' '.join(str(it + 1) for it in addresses)

def solve(input_name, output_name):
    global input_file
    tstart = time.clock()
    with open(input_name, 'r') as input_file, open(output_name, 'w') as output_file:
        casecount = readint()
        
        for case in range(1, casecount + 1):
            s = solvecase()
            s = "Case #%d: %s" % (case, str(s)) 
            print(s, file=output_file)
            print(s) 
        
    print('%s solved in %.3f' % (input_name, time.clock() - tstart))


def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
