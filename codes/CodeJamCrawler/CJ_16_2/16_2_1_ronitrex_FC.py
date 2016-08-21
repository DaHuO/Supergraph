from itertools import groupby
from collections import Counter
import math
import itertools
from string import ascii_lowercase
import re

from operator import itemgetter

def subtraction(X):
    flag = True
    S1 = S.copy()
    for k in X:
        if k in S1:
            S1.remove(k)
        else:
            flag = False
            break
    return flag

def remove(Y):
    for k in Y:
        S.remove(k)

L1 = [[0, "ZERO"],[2,"TWO"],[4,"FOUR"],[6,"SIX"],[8,"EIGHT"]]
L2 = [[1, "ONE"],[3,"THREE"],[5, "FIVE"],[7,"SEVEN"]]
L3 = [[9, "NINE"]]

N = int(input())
for _ in range(N):
    S = list(input())
    S0 = S.copy()
    Num = ''

    for l in L1:
        while subtraction(l[1]):
            remove(l[1])
            Num += str(l[0])
    for l in L2:
        while subtraction(l[1]):
            remove(l[1])
            Num += str(l[0])
    for l in L3:
        while subtraction(l[1]):
            remove(l[1])
            Num += str(l[0])

    print('Case #{}: {}'.format(_+1, ''.join(sorted(Num))))




