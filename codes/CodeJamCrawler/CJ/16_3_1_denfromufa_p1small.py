from __future__ import print_function
import sys
from string import ascii_uppercase

sys.setrecursionlimit(10000)


def condit(tpl):
    s = sum(tpl)
    for t in tpl:
        if (2 * t) > s:
            return False
    return True


def solve(tpl, route=()):
    if sum(tpl) == 0:
        return route
    for i1, t1 in enumerate(tpl):
        for i2, t2 in enumerate(tpl):
            if (t1 > 0) and (t2 > 0):
                tpli = tuple((_ if (j not in (i1, i2)) else _ - 1)
                             for j, _ in enumerate(tpl))
                if not condit(tpli):
                    print('bad leftover {}'.format(tpli))
                    continue
                # TODO: check for 50% condition
                # TODO: if fails, use pair selection with product()
                if i1 == i2:
                    routei = route + (ascii_uppercase[i1],)
                else:
                    routei = route + (ascii_uppercase[i1] +
                                      ascii_uppercase[i2],)
                print(tpli, routei)
                return solve(tpli, routei)

with open(r"/home/dta/Downloads/jam/p1input.txt", mode='r') as f1:
    finput = f1.readlines()
T = int(finput[0])
# print(T)
if len(finput) != (2 * T + 1):
    raise Exception("bad input file")
with open(r"/home/dta/Downloads/jam/p1output1.txt", mode='w') as f2:
    l = 0
    for x in range(1, T + 1):
        l += 1
        N = int(finput[l].strip())
        # print(N)
        l += 1
        P = tuple(map(int, finput[l].strip().split(' ')))
        print(P)
        sol = solve(P)
        print(sol)
        # TODO: confirm facts
        # if not confirmfacts(S, sol):
        #    raise Exception('wrong number {} for string {}'.format(sol, S))
        f2.write("Case #{x}: {y}\n".format(x=x, y=", ".join(list(sol))))
