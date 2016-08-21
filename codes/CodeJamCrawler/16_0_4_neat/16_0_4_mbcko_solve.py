#!/usr/bin/env python

import sys

def solve(*args):
    (K, C, S) = args
    
    # trivial
    if C == 1 or K == 1:
        if S < K:
            return "IMPOSSIBLE"
        else:
            res = range(1, K + 1)
    else:
        if (S < K - C):
            return "IMPOSSIBLE"
        else:
            get = lambda i: (i*K + i + 2)
            ktoc = K**C
            res = (get(i) for i in range(S) if get(i) <= ktoc)
    
    return " ".join(str(one) for one in res)

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        params = [int(one.strip()) for one in sys.stdin.readline().split(" ")]
        result = solve(*params)
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


