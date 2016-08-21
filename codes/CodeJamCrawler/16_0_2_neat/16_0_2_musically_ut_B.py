#!/usr/bin/env python
T = int(input())

i = 1
while i <= T:
    cakes = input()
    while len(cakes) > 0 and cakes[-1] == '+':
        cakes = cakes[:-1]

    if len(cakes) == 0:
        print("Case #{}: 0".format(i))
    else:
        flips = 1
        for (x, y) in zip(cakes[:-1], cakes[1:]):
            if x != y:
                flips += 1
        print("Case #{}: {}".format(i, flips))

    i += 1

