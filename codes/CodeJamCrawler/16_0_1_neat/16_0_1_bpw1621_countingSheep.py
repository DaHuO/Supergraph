#!/usr/bin/env python

from __future__ import print_function

import sys


class CountingSheep( object ):
    def __init__( self, inputFile, outFile ):
        self.digitCounts = []

        with open( inputFile, 'r' ) as i, open( outFile, 'w+' ) as o:
            inputFileContents = i.readlines()
            numberOfCases = inputFileContents[ 0 ]
            for case in inputFileContents[ 1: ]:
                self.count( int( case ) )
            self.printCounts( o )

    def count( self, number ):
        self.digitCounts.append( 'INSOMNIA' )

        # special case
        if number == 0:
            return

        digitDict = { 0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False }
        for i in xrange( 1, sys.maxint ):
            nextNumber = i * number
            for c in str( nextNumber ):
                digitDict[ int( c ) ] |= True

            if( all( digitDict.values() ) ):
                self.digitCounts[ -1 ] = nextNumber
                break

    def printCounts( self, outFile ):
        for caseNumber, digitCount in enumerate( self.digitCounts ):
            print( 'Case #' + str( caseNumber + 1 ) + ': ' + str( digitCount ), file = outFile )

if __name__ == '__main__':
    #countingSheep = CountingSheep( 'countingSheepTestInput.txt', 'results.txt' )
    #countingSheep = CountingSheep( 'A-small-attempt0.in', 'results-small.txt' )
    countingSheep = CountingSheep( 'A-large.in', 'results-large.txt' )

