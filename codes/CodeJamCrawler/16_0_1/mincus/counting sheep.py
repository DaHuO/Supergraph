#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def solve( n ):
    if n == 0:
        return "INSOMNIA"

    found = False
    found_nums = np.zeros( ( 10 ) )
    new_num = 0
    tmp = 0
    cnt = 1

    while np.sum( found_nums ) != 10:
        new_num = np.dot( cnt, n )
        cnt += 1

        tmp = new_num
        while tmp > 0:
            dig = np.mod( tmp, 10 )
            tmp = np.floor_divide( tmp, 10 )
            found_nums[ dig ] = 1

    return new_num

if __name__ == "__main__":
    testcases = int( input() )

    for caseNr in range( 1, testcases + 1 ):
        n = int( input() )
        print( "Case #%i: %s" % ( int( caseNr ), solve( n ) ) )