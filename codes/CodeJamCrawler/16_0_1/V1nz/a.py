from sys import *
from math import *

def solve(case, n) :
    nb_essai = 1000000
    nb_vu = set()
    nb_actuel = n
    my_bool = False
    for j in range(1, nb_essai) :
        nb_actuel = n * j
        car = str(nb_actuel)
        for k in car :
            nb_vu.add(k)
        if "0" in nb_vu and "1" in nb_vu and "2" in nb_vu and "3" in nb_vu and "4" in nb_vu and "5" in nb_vu and "6" in nb_vu and "7" in nb_vu and "8" in nb_vu and "9" in nb_vu :
            print("Case #{0}: {1}".format(case+1, nb_actuel))
            my_bool = True
            break
    # print("Case #{0}: {1}".format(case+1, nb_invite))
    # if "0" in nb_vu and "1" in nb_vu and "2" in nb_vu and "3" in nb_vu and "4" in nb_vu and "5" in nb_vu and "6" in nb_vu and "7" in nb_vu and "8" in nb_vu and "9" in nb_vu :
        # print("Case #{0}: {1}".format(case+1, nb_actuel)
    if not my_bool :
        print("Case #{0}: INSOMNIA".format(case+1))

cases = int(input())
for i in range(cases) :
    n = int(input())
    solve(i, n)
