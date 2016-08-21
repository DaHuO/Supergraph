# keep track of each number seen - use set
# starts with N, multiply by it in a for loop, count digits until all are in set
# 2,4,6,8,10,12,14,16,18,20
# 1,2,3,4,5,6,7,8,9,0
# x,x,x,x,x,x,,x,x,x,x
#Last number: 90
# 3,6,9,12,15,18,21,..
# 0,0,

# 30, 33, 36,
# Theory: Once you go through 1xN to 9xN if you don't have all digits, you will never get them
# WRONG: see example inputs

# Theory: Only 0 will make her count forever

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(N):
    seen = set()
    if N == 0:
        return "INSOMNIA"
    i = 1
    while len(seen) != 10:
        cur = i*N
        i+=1
        for c in str(cur):
            seen.add(int(c))
    return cur

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(int(cipher))))
