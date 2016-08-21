#!/usr/bin/env python

from __future__ import division, print_function
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        
        if N == 0:
            print('Case #%d: INSOMNIA' % (i + 1))
        else:
            digits = set()
            k = 0
            
            while len(digits) < 10:
                k += 1
                digits.update(list(str(k * N)))
            
            print('Case #%d: %d' % (i + 1, k * N))