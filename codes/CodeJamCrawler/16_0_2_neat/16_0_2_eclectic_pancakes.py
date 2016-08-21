#!/usr/bin/python3

import sys

T = int(input())
stacks = [line.strip() for line in sys.stdin.readlines()]

def CheckStack(S):
    return sum(S) == len(S)

def ReduceStack(S):
    S = S.rstrip('+') # ignore correct bottom
    lenS = len(S)
    for i_S in range(lenS-1): # ignore substacks of same orientation
        if S[lenS-i_S-1] == S[lenS-i_S-2]:
            S = S[:lenS-i_S-2]+ S[lenS-i_S-1:]
    return S

test = False
for i_T in range(T):
    S = stacks[i_T]
    lenS = len(S)
    Sp = ReduceStack(S)
    res = len(Sp)
    n = len(Sp)//2
    if test:
        if len(Sp) % 2 == 0:
            print('even', '(+-)_n with n = %d \'%s\''%(n, Sp), 'res = ', res)
        else:
            print('odd', '-(+-)_n with n = %d \'%s\''%(n, Sp), 'res = ', res)
    else:
        print("Case #{}: {}".format(i_T+1, res))

