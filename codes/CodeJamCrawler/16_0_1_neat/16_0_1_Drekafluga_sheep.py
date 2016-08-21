#! /usr/bin/python3


import sys
t = int(input())
def valmis(a):
    return a[1:] == a[:-1]
for i in range(1, t + 1):
    algnen = int(input())
    n = algnen
    loetud = [False, False, False, False, False, False, False, False, False, False]
    for nr in str(n):
        loetud[int(nr)] = True
    if n > 0:
        while not valmis(loetud):
            n = n + algnen
            for nr in str(n):
                loetud[int(nr)] = True
    else:
        n = "INSOMNIA"
    print("Case #{}: {}".format(i, n))

sys.exit()
