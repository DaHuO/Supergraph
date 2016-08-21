#!/usr/bin/env python

import sys

def solve(*args):
    (S,) = args
    
    R = S[0]
    
    for s in S[1:]:
        if s >= R[0]:
            R = s + R
        else:
            R += s
    
    return R

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        params = [one.strip() for one in sys.stdin.readline().split(" ")]
        result = solve(*params)
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


