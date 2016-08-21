#!/bin/python3
import sys

index = 1

num = input()
for line in sys.stdin.readlines():
    print("Case #" + str(index), end=': ')
    index += 1

    timesflipped = 0

    thechar = '-'
    k = line.rfind(thechar)
    thechar = '+'

    while k != -1:
        k = line.rfind(thechar, 0, k)
        timesflipped += 1
        if thechar == '-':
            thechar = '+'
        else:
            thechar = '-'


    print(str(timesflipped))
