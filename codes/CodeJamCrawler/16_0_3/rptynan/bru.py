#!/usr/bin/python3
from numpy import base_repr
from math import ceil, sqrt
import sys

def check(current):
    divs = []
    for base in range(2,11):
        num = int(current, base)
        for div in range(2, 2000): # ceil(sqrt(num)) + 1):
            if num % div == 0:
                divs += [str(div)]
                break
        if len(divs) != base - 1:
            return (False, [])
    return (True, divs)



# for test in ['100011', '111111', '111001', '110011',     '110111'] :
#     print(check(test))

T = int(input())
N, J = [int(s) for s in input().split(" ")]

cur = '1' + '0' * (N-2) + '1'
print('Case #1:')

while J > 0:
    (works, divs) = check(cur)
    if works:
        print('{} {}'.format(cur, ' '.join(divs)))
        sys.stdout.flush()
        J -= 1
    cur = base_repr(int(cur, 2) + 2, 2)
