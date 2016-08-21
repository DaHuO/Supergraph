#!/usr/bin/python3

from operator import itemgetter

cases = int(input())
party = []

def answer(case, a):
    print("Case #{}: {}".format(case + 1, a))

def pop_sen(i, n):
    global party
    name, size = party[i]
    size -= n
    party[i] = name, size
    return "".join((party[i][0] + " ")*n)

for case in range(cases):
    res = ""
    _ = int(input())
    global party
    party = [(chr(int(a)+65), int(b)) for (a,b) in enumerate(input().split())]

    party.sort(key=itemgetter(1), reverse=True)
    n = party[0][1] - party[1][1]
    if n:
        res += pop_sen(0, n)
    reversed(party)
    while len(party) > 2:
        res += pop_sen(-1, party[-1][1])
        del party[-1]
    res += "".join((party[0][0]+party[1][0] + " ") * party[0][1]).strip()

    print("Case #{}: {}".format(case + 1, res.strip()))

