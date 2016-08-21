#!/usr/bin/env python

import time
import sys
#@profile
def repl(s):
    return s.replace("+", ".").replace("-", "+").replace(".", "-")
    
#@profile
def flip(s):
    return repl("".join(reversed(s)))
    
#@profile
def solve(*args):
    (S,) = args
    
    # trivial cases
    if "-" not in S:
        return 0
    if "+" not in S:
        return 1
        
    retval = 0
    s = S
    while True:
        f = s.find(repl(s[0]))
        
        s = flip(s[0:f]) + s[f:]
        retval += 1

        if "-" not in s:
            break
        if "+" not in s:
            retval += 1
            break
    
    return retval
    

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
       result = solve(sys.stdin.readline().strip())
       print "Case #%d: %s" % (caseNumber, result)
       
    # for caseNumber in range(10000):
    #     result = solve(caseNumber)
    #     print "Case #%d: %s" % (caseNumber, result)

if __name__ == '__main__':
    main()


