#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def solve( stk ):
    pattern1 = re.compile( '^-+$' )
    pattern2 = re.compile( '(?=\+-+\+)' )

    stk = re.sub( '-\++$', '-', stk )
    count = 0
    if ( pattern1.match( stk ) ):
        count = 1
    else:
        count += stk.count( '-+' )
        count += ( stk.count( '+-' ) * 2 )
        count -= len( pattern2.findall( stk ) )

    return count

if __name__ == "__main__":
    testcases = int( input() )

    for caseNr in range( 1, testcases + 1 ):
        stk = input()
        print( "Case #%i: %s" % ( int( caseNr ), solve( stk ) ) )