#!/usr/bin/python3

import math
import itertools

f = open("test.in", 'r')
lines = f.readlines()
f.close()

def isPrime(n):
    if n == 2 or n == 3:
        return -1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return x
    return -1

def binToBaseToDec(b, base):
    i = len(b)-1
    j = 0
    res = 0
    while i >= 0:
        res += int(b[i]) * math.pow(base, j)
        j += 1
        i -= 1
    return res

nb = 0
i = 0
for line in lines:
    if i == 0:
        nb = int(line)
    if i > 0:
        print("Case #1:")
        nj = line.split(" ")
        combi = ["".join(seq) for seq in itertools.product("01", repeat=int(nj[0]))]
        combi.pop(0)
        combi.pop(0)
        count = 0
        for comb in combi:
            if comb[0] != "1" or comb[len(comb) - 1] != "1":
                continue
            if count >= int(nj[1]):
                break
            base = []
            div = []
            found = True
            for k in range(2, 11):
                base.append(binToBaseToDec(comb, k))
                d = isPrime(base[len(base) - 1])
                if d == -1:
                    found = False
                    break
                div.append(d)
            if not found:
                continue
            count += 1
            print(comb + " ", end="")
            for x in range(len(div)):
                if x == len(div) - 1:
                    print("{0}".format(div[x]))
                else:
                    print("{0} ".format(div[x]), end="")
    i += 1
