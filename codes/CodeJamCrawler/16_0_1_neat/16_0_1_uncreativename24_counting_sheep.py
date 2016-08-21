#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cases = int(input().strip())

for i, line in enumerate(range(cases), 1):
    number = input().strip()

    if int(number) == 0:
        print("Case #{0:s}:".format(str(i)), 'INSOMNIA')
    else:
        current_L = list(map(int, number))
        current_S = ''.join(str(x) for x in current_L)
        seen = set(current_L)

        counter = 1
        while len(seen) < 10:
            temp = int(number) * counter
            current_S = str(temp)
            current_L = list(map(int, current_S))
            seen |= set(current_L)
            counter += 1

        print("Case #{0:s}:".format(str(i)), current_S)
