#!/usr/bin/python

import os
import sys
import re
import itertools
import collections
import copy
import fractions
import bisect
import decimal
import math
import random

# decimal.getcontext().prec = 50
# sys.setrecursionlimit(10000)

def solve(f, skip=False):
    n, r, p, s = f.read_int_list()
    if skip: return 0

    for p1,p2 in itertools.combinations(['R','P','S'], 2):
        h = p1+p2
        for i in xrange(n-1):
            hold = h[:]
            h = ""
            for hh in hold:
                if hh == 'R':
                    h += 'RS'
                elif hh == 'P':
                    h += 'PR'
                else:
                    h += 'PS'

        c = collections.Counter(h)
        if c['R']==r and c['P']==p and c['S']==s:
            for j in xrange(1,n+1):
                for i in xrange(0,len(h),2**j):
                    if h[i:i+2**(j-1)] > h[i+2**(j-1):i+2**j]:
                        h = h[:i] + h[i+2**(j-1):i+2**j] + h[i:i+2**(j-1)] + h[i+2**j:]
            return h

    return "IMPOSSIBLE"

class Reader(object):
    def __init__(self, filename):
        self.f = open(filename)
        self.linenum = 1

    def read_int(self):
        self.linenum += 1
        return int(self.f.readline().strip())
    def read_float(self):
        self.linenum += 1
        return float(self.f.readline().strip())
    def read_decimal(self):
        self.linenum += 1
        return decimal.Decimal(self.f.readline().strip())
    def read_str(self):
        self.linenum += 1
        return self.f.readline().strip()

    def read_int_list(self):
        self.linenum += 1
        return map(int, self.f.readline().split())
    def read_float_list(self):
        self.linenum += 1
        return map(float, self.f.readline().split())
    def read_decimal_list(self):
        self.linenum += 1
        return map(decimal.Decimal, self.f.readline().split())
    def read_str_list(self):
        self.linenum += 1
        return self.f.readline().split()

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else sys.argv[0].replace('.py', '-sample.in')
    cnum = int(sys.argv[2]) if len(sys.argv) > 2 else None
    output = filename[:-3]+'.out' if filename[-3:] == '.in' else filename+'.out'
    f = Reader(filename)
    cases = f.read_int()

    if cnum:
        for case in xrange(cases):
            if cnum == case+1:
                print '(line: %d) '%f.linenum
                line = 'Case #%d: %s\n'%(case+1,str(solve(f)))
                print line,
            else:
                solve(f, skip=True)
    else:
        g = open(output, 'w')
        for case in xrange(cases):
            line = 'Case #%d: %s\n'%(case+1,str(solve(f)))
            g.write(line)
            print line,
