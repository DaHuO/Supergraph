from sys import *
from math import *

def solve(case, mot) :
    solus = mot[0]
    for i in range(1, len(mot)) :
        if mot[i] >= solus[0] :
            solus = mot[i] + solus
        else :
            solus = solus + mot[i]
    print("Case #{0}: {1}".format(case, solus))

cases = int(input())
for i in range(1, cases + 1) :
    tab = input()
    solve(i, tab)
