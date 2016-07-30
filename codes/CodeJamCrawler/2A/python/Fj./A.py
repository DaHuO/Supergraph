# from __future__ import division, print_function

import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'A'
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

winner = {
        'rr': '' , 'rp': 'p', 'rs': 'r', 
        'pr': 'p', 'pp': '' , 'ps': 's', 
        'sr': 'r', 'sp': 's', 'ss': '' ,
        } 
        

def update_best(best, left, right):
    for l_winner, l_s in left:
        for r_winner, r_s in right:
            w = winner[l_winner + r_winner]
            if w:
                s = l_s + r_s
                if best.get(w, 'z') > s:
                    best[w] = s

mem = {}
def solve_rec(r, p, s):
    total = r + p + s
    if total == 1:
        if r:
            return [['r', 'r']]
        elif p:
            return [['p', 'p']]
        else:
            return [['s', 's']]
        
    mem_key = (total, r, p)
    best = mem.get(mem_key, None)
    if best is not None:
        return best
    
    half_total = total // 2
    best = {}
    for r1 in range(0, r + 1):
        for p1 in range(0, p + 1):
            s1 = half_total - r1 - p1
            if 0 <= s1 <= s:
                left = solve_rec(r1, p1, s1)
                right = solve_rec(r - r1, p - p1, s - s1)
                update_best(best, left, right)
    
    mem[mem_key] = best = sorted(best.items())
#     print(mem_key, best)
    return best

def solve_rec_fast(r, p, s):
    if max(abs(r - p), abs(r - s), abs(s - p)) > 1: return []   
    total = r + p + s
    if total == 1:
        if r:
            return [['r', 'r']]
        elif p:
            return [['p', 'p']]
        else:
            return [['s', 's']]
        
    mem_key = (total, r, p)
    best = mem.get(mem_key, None)
    if best is not None:
        return best

    avg = total // 6    
    best = {}
    for r1 in range(avg, avg + 2):
        for p1 in range(avg, avg + 2):
            s1 = total // 2 - r1 - p1
            if 0 <= s1 <= s:
                left = solve_rec_fast(r1, p1, s1)
                right = solve_rec_fast(r - r1, p - p1, s - s1)
                update_best(best, left, right)
    
    mem[mem_key] = best = sorted(best.items())
#     print(mem_key, best)
    return best

def main2():
    total = 1024
    for r in range(0, total + 1):
        for p in range(0, total - r + 1):
            solve_rec_fast(r, p, total - r - p) 
    for x in sorted(mem.items()):
        if x[1]:
            print(x)
    
# main2()
# sys.exit()
                        
def solvecase():
    N, R, P, S = readintlist()
    assert S + R + P == 2 ** N
    best = solve_rec_fast(R, P, S)
    if not best:
        return 'IMPOSSIBLE'
    res = min(v for _, v in best).upper()
    return res


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
