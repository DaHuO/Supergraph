#!/usr/bin/python
from sys import stdin

def translate(string):
    result = []
    for x in string:
        if x == '-':
            result.append(False)
        else:
            result.append(True)
    return result

def compute(array):
    res = 0
    for i, x in enumerate(array):
        if not x:
            for j in range(i, len(array)):
                array[j] = not array[j]
            res += 1
    return res

for i in range(input()):
    # remove the newline and reverse the string
    print "Case #{}: {}".format(i + 1, compute(translate(stdin.readline()[:-1][::-1])))