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

INPUT = "sample_in.txt"
OUTPUT = "output.txt"
CASE_SEP = '\n'

def main():
    cases = parseCases(INPUT, parser, printout=True)
    results = runCases(cases, runCase, printout=True, casesep = CASE_SEP)
    writeResults(OUTPUT, results, casesep = CASE_SEP)
    
def parser(rowsIter):
    return [int(e) for e in rowsIter.next().split(' ')]

def getJamCoinDividors(s):
    divs = [None]*9
    for k in range(2,11):
        isP, div = isPrime(int(s,k))
        if isP: return None
        divs[k-2]=div
    return divs

def runCase(case):
    n, j = case
    
    jamCoins = []
    for i in xrange(2**(n-2)):
        s = '1'+"{num:0{width}b}".format(num=i,width=n-2)+'1'
        
        failed = False
        try:
            with Timeout(seconds=1):
                divs = getJamCoinDividors(s)
        except TimeoutError:
            failed = True
            continue
        finally:
            if failed:
                print len(jamCoins),s, '*** aborted ***'
            elif divs:
                jamCoins.append([s]+map(str,divs))
                print len(jamCoins),s,divs
            else:
                pass
                #print s,'---'
        if len(jamCoins)>=j: break
    
    return '\n'.join([' '.join(e) for e in jamCoins])

from functools import wraps
import errno
import os
import signal
class TimeoutError(Exception):
    pass
class Timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

import collections
import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

#@memoized
def isPrime(num):
    assert num>=3
    if num == 3: return True, None
    if num%2 == 0: return False, 2
    if num < 9: return True, None
    if num%3 == 0: return False, 3
    r = int(num**0.5)
    f = 5
    while f <= r:
        if num%f == 0: return False, f
        if num%(f+2) == 0: return False, f+2
        f +=6
    return True, None

if __name__=="__main__":
    main()
