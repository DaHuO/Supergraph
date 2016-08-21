import pdb
import sys
import re
import time
from collections import namedtuple
import itertools
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

def compute_distribution(probs):
    current = {0: 1.0}
    for p in probs:
        current = {i: current.get(i, 0.0) * (1 - p) + current.get(i - 1, 0.0) * p
                for i in range(len(current) + 1)}
    return current
        
def compute_stalemate_prob(n, d1, d2):
    return sum(p * d2.get(n - cnt, 0.0) for cnt, p in d1.items())
    
def zzz(base_probs, K):
    K_2 = K // 2
    for selection in itertools.combinations(base_probs, K):
        d1 = compute_distribution(selection[0 : K_2])
        d2 = compute_distribution(selection[K_2 : K])
        yield compute_stalemate_prob(K_2, d1, d2)
    
def solvecase():
    N, K = readintlist()
    base_probs = list(map(float, readstr().split()))
    assert len(base_probs) == N
    return max(zzz(base_probs, K))


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
