#!/bin/python

T = int(input())

for i in range(T):
    line = input()
    sign = line[0]
    swaps = 0
    for l in line:
        if l != sign:
            swaps += 1
            sign = l
    if sign != '+':
        swaps += 1

    print("Case #" + str(i+1) + ": " + str(swaps))
