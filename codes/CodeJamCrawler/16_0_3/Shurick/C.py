#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from itertools import izip
import random
from sympy import *


def get_random_coeffs(N):
    C = [random.randint(0, 1) for __ in range(N-2)]
    C.insert(0, 1)
    C.append(1)
    return C


def poly_template(N):
    P = ['x**%d' % n for n in range(N-1, 1, -1)]
    P.append('x')
    P.append('1')
    return P


def get_poly(coeffs, P_template):
    P = []
    for c, p in izip(coeffs, P_template):
        if c == 1:
            P.append(p)
    return ' + '.join(P) 
    

def solve(N, J):
    PT = poly_template(N)
    
    A = {}
    while len(A) < J:
        C = get_random_coeffs(N)
        P = get_poly(C, PT)
        F = factor(P)
        F = F.as_ordered_factors()
        if len(F) == 1:
            continue
        jamcoin = ''.join(map(str, C))
        #print >> sys.stderr, F
        A[jamcoin] = F
        #if len(A) % 10 == 0:
        #    print >> sys.stderr, 'found %d polynomials' % len(A)
    
    J = {}
    for jc, F in A.iteritems():
        f = F[0]
        J[jc] = [f.subs('x', b) for b in range(2, 11)]
        
    return J


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


ifs.readline() # skip T == 1

N, J = numbers_from_line()

a = solve(N, J)

ofs.write('Case #1:\n')
for jamcoin, factors in a.iteritems():
    ofs.write('%s %s\n' % (jamcoin, ' '.join(map(str, factors))))
