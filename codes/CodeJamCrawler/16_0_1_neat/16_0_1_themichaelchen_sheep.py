#!/bin/python3
import math

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        curr_num = n
        numbers_seen = set()
        while len(numbers_seen) < 10:
            digits = list(str(curr_num))
            for d in digits:
                numbers_seen.add(d)
            curr_num += n
        return str(curr_num-n)

num_cases = int(input())
for casenum in range(1, num_cases+1):
    n = int(input())
    
    res = solve(n)
    print ("Case #{0}: {1}".format(casenum, res))