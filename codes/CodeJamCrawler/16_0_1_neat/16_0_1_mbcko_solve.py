#!/usr/bin/env python

import sys

def solve(*args):
    (N,) = args
    
    # trivial case
    if N == 0:
        return "INSOMNIA"
        
    n = N
    seen = set(str(n))
    while True:
        n += N
        seen.update(str(n))

        if len(seen) == 10:
            break
    
    return n

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
       result = solve(int(sys.stdin.readline().strip()))
       print "Case #%d: %s" % (caseNumber, result)
       
    # for caseNumber in range(10000):
    #     result = solve(caseNumber)
    #     print "Case #%d: %s" % (caseNumber, result)

if __name__ == '__main__':
    main()


