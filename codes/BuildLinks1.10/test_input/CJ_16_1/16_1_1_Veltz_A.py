'''
Created on Apr 16, 2016

@author: doronv
'''

# import section

import sys
import re
from certifi import __main__

def maxAB(S):
    if len(S) == 0:
        return ''

    c = max(S)
    prevP = 0
    for m in re.finditer(c, S):
        p = m.span()[0]
        if prevP == 0:
            o = c + maxAB(S[:p])
        else:
            o = c + o + S[prevP:p]
    #concatenate the rest of the string
    return o + S[(S.rfind(c) + 1):]

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        # read S
        S = inputFile.readline().rstrip()

        O = maxAB(S)

        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + O + '\n'
        outputFile.write(OutputLine)

if __name__ == '__main__':
    inputFile = open(sys.argv[1], 'r')
    outputFile = open(sys.argv[2], 'w')
    solve(inputFile, outputFile)