# -*- coding: utf-8 -*-
"""
Problem A. 
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
    n, r, p, s = readints(f)
    return (r, p, s, n)

def solvecase(case):
    (r, p, s, n) = case
    if max(r, p, s) != min(r, p, s) + 1:
        return 'IMPOSSIBLE'
    return bestout(n, (p, r, s))

def bestout(n, prs):
    if n == 1:
        return ''.join(c for c, i in zip('PRS' ,prs) if i)
    if n & 1:
        i = prs.index(min(prs))
        k = prs[i]//2
        half = []
        for j in range(3):
            if i != j:
                prs1 = [k, k, k]
                prs1[j] += 1
                half.append(bestout(n-1, prs1))
    else:
        i = prs.index(max(prs))
        k = prs[i]//2
        half = []
        for j in range(3):
            if i != j:
                prs1 = [k, k, k]
                prs1[j] -= 1
                half.append(bestout(n-1, prs1))    
    if half[0] > half[1]:
        half = reversed(half)
    return ''.join(half)  
	
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
