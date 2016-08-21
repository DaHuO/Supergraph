# -*- coding: utf-8 -*-
"""
Problem B. 
uses python 3.4.1

@author: Eric Kuritzky
"""
from collections import *
import itertools as ito
import operator as op
import functools as ft
from sys import argv, stdin, stdout, stderr, setrecursionlimit

#setrecursionlimit(1000000)

errprt = ft.partial(print, file=stderr)    
    
def readcase(f):
    n, k = readints(f)
    p = list(map(float, f.readline().strip().split(' ')))
    return p, k

def solvecase(case):
    p, k = case
    return max(probtie(comb) for comb in ito.combinations(p, k))

def probtie(p):
    c = convolveall(p)
    return c[len(p)//2]

def convolveall(p):
    if len(p) == 1:
        return (p[0], 1-p[0])
    k = len(p)//2
    c1, c2 = convolveall(p[:k]), convolveall(p[k:])
    ans = [0]*(len(p)+1)
    for i, x1 in enumerate(c1):
        for j, x2 in enumerate(c2):
            ans[i+j] += x1*x2
    return ans
	
def readints(f):
    return list(map(int, f.readline().strip().split(' ')))

def readflds(f, types):
    if isinstance(types, tuple):
        return [typ(fld) for fld, typ
                in zip(f.readline().strip().split(),
                       ito.chain(types, ito.repeat(types[-1])))]
    else:
        return [types(fld) for fld in f.readline().strip().split()]

def main():
    with open(argv[1]) as f, open('out', 'w') as out:
        cases = int(f.readline())
        for ncase in range(1, cases+1):
            case = readcase(f)
            soln = solvecase(case)
            if len(argv) > 2:
                print('Case #%d: %s' % (ncase, soln))
            print('Case #%d: %s' % (ncase, soln), file=out)

from datetime import datetime

start = datetime.now()
print(str(start))
main()
stop = datetime.now()
print(str(stop-start))
