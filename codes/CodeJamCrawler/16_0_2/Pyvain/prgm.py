# -*- coding: utf-8 -*-


def solve(pile):
    slices = []
    while pile != "":
        starting = pile[0]
        i = 0
        while i < len(pile) and pile[i] == starting:
            i += 1
        slices.append(pile[:i])
        pile = pile[i:]
    nb = 0
    while len(slices) > 1:
        if slices[0][0] == "-":
            nb += 1
            slices[1] = "+"*(len(slices[0])+len(slices[1]))
            slices.pop(0)
        else:
            nb += 1
            slices[1] = "-"*(len(slices[0])+len(slices[1]))
            slices.pop(0)
    return nb if slices[0][0] == "+" else (nb+1)




t = int(input())
for i in range(t):
    pile = input()
    print("Case #" + str(i+1) + ": " + str(solve(pile)))
