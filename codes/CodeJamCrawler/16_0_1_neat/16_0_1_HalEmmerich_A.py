#!/bin/python3

runs = int(input())



for i in range(runs):

    integers = set()
    n = int(input())
    x = 1
    while len(integers) != 10:
        y = n * x
        x += 1
        if y == 0:
            break
        for num in str(y):
            if num not in integers:
                integers.add(num)

    if y != 0:
        print("Case #" + str(i+1) + ": " + str(y))
    else:
        print("Case #" + str(i+1) + ": " + "INSOMNIA")
exit()
