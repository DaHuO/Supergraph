#!/usr/bin/env python
import fileinput


def bleatrix(x):
    if x == 0:
        return "INSOMNIA"
    numbers = [False] * 10
    y = str(x).strip("0")
    for char in str(y):
        numbers[int(char)] = True
    i = 1
    while not all(num for num in numbers):
        i += 1
        y = i * x
        for char in str(y):
            numbers[int(char)] = True
    return str(i*x)

i = 0
for line in fileinput.input():
    if i == 0:
        i += 1
        continue
    print("Case #" + str(i) + ": " + bleatrix(int(line)))
    i += 1
