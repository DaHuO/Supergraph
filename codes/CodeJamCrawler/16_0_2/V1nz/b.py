from sys import *
from math import *

def solve(case, pile) :
    nb_move = 1
    actuel = pile[0]
    for i, j in enumerate(pile) :
        precedent = actuel
        actuel = pile[i]
        if precedent != actuel :
            nb_move += 1
    if pile[-1] == "+" :
        nb_move -= 1
    print("Case #{0}: {1}".format(case+1, nb_move))

cases = int(input())
for i in range(cases) :
    pile = str(input())
    solve(i, pile)
