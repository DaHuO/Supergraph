import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'B'
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
    cstr, jstr = readstr().split()
    n = len(cstr)
    assert n == len(jstr)
    cre = re.compile(cstr.replace('?', '.') + '$')
    jre = re.compile(jstr.replace('?', '.') + '$')
    digits = '0123456789'
    best = (1e9, 0, 0)
    for cdigits in product(* [digits] * n):
        cs = ''.join(cdigits)
        if not cre.match(cs): continue
        for jdigits in product(* [digits] * n):
            js = ''.join(jdigits)
            if not jre.match(js): continue
            c, j = int(cs), int(js)
            new = (abs(c - j), cs, js)
            if new < best:
                best = new
    return best[1] + ' ' + best[2]


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
