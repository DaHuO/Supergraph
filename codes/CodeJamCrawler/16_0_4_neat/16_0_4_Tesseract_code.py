from __future__ import division
from pylab import *
import time, os
from copy import deepcopy
from pprint import pprint, pformat

'''
input:
    path: path to input file
    parser: function:
        input:
            list of the rows of the input file
        returns:
            one parsed case
        NOTE: only use the lines from the iterator corresponding with current case being parsed
returns:
    list of cases with parsed cases returned by provided parser-function
'''
def parseCases(path, parser, printout=False):
    if not os.path.isfile(path):
        print printSubject("ERROR", "No input file found!", error=True)
        return []
    
    # get rows without newline from file and make iterator
    with open(path) as fil:
        rows = fil.readlines()
        rows = [row.rstrip() for row in rows]
    rowsIter = iter(rows)
    
    if not rows:
        print printSubject("ERROR", "Input file is empty!", error=True)
        return []
    
    # parse cases
    nrOfCases = int(rowsIter.next())
    parsedCases = [parser(rowsIter) for i in range(nrOfCases)]
    
    # printout if needed
    if printout:
        printSubject("Parsed Cases", pformat(parsedCases))
    return parsedCases

def runCases(cases, runCase, printout=False, casesep='\n'):
    tic = time.time()
    # run
    results = [runCase(case) for case in cases]
    totalTime = time.time() - tic
    
    # printout if needed
    if printout:
        printResults(results, casesep=casesep)
        print "Total time: {:.3f} s".format(totalTime)
    return results

def printResults(results, printout=True, casesep='\n'):
    # build string
    resultsString = '\n'.join(["Case #{}:{}{}".format(i+1, casesep, caseResult) for i,caseResult in enumerate(results)])
    
    # printout if needed
    if printout:
        printSubject("Results", resultsString)
    return resultsString

def writeResults(path, results, casesep='\n'):
    with open(path,'w') as fil:
        fil.write(printResults(results, printout=False, casesep=casesep))

def printSubject(title, content, error=False):
    title = ' '+title+' '
    dividerLength = max(len(title), 60)
    print "{title:{div}^{dividerLength}}\n{content}\n{empty:{div}^{dividerLength}}\n".format(div='-' if not error else '|', title=title, content=content, dividerLength=dividerLength, empty="")

###########################################################################################################################

INPUT = "D-small-attempt0.in"
OUTPUT = "output.txt"
CASE_SEP = ' '

def main():
    cases = parseCases(INPUT, parser, printout=True)
    results = runCases(cases, runCase, printout=True, casesep = CASE_SEP)
    writeResults(OUTPUT, results, casesep = CASE_SEP)
    
def parser(rowsIter):
    return [int(e) for e in rowsIter.next().split(' ')]

def runCase(case):
    k,c,s = case
    
    return ' '.join([str(i*k**(c-1)+1) for i in range(k)])

if __name__=="__main__":
    main()
