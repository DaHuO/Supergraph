#! /usr/bin/env python

import math
import itertools

#  +---+---+---+
#  | a | b | c |
#  +---+---+---+
#  0   1   2   3
# -3  -2  -1
        
if __name__ == "__main__":
    T = int( input() )
    
    for x in range(1,T+1):
        
        N = int(input())
        if N == 0:
            print('Case #%i: INSOMNIA' % (x))
        else:
            S = set(['0','1','2','3','4','5','6','7','8','9'])
            i = 1
            while S:
                R = i * N
                D = set(str(R))
                S = S - D
                i = i + 1
            print('Case #%i: %i' % (x,R))