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
import functools
import sys
sys.setrecursionlimit(15000)
@functools.lru_cache(maxsize=None)
def solve(S):
    if len(S) == 0:
        return S
    else:
        left = solve(S[1:])+S[0]
        right = S[0]+solve(S[1:])
        return left if left > right else right

if __name__ == "__main__":
    testcases = int(input())

    for caseNr in range(1, testcases+1):
        cipher = input()
        print("Case #%i: %s" % (caseNr, solve(cipher[::-1])))



# recursive left, mid, right

