#!/usr/bin/env python
import fileinput

def pancakes(stack):
    s = stack[0:-1]
    if len(s) == 1:
        if s[0] == "+":
            return 0
        else:
            return 1
    n = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            n += 1
    if s[-1] == "-":
        n += 1
    return n

i = 0
for line in fileinput.input():
    if i == 0:
        i += 1
        continue
    print("Case #" + str(i) + ": " + str(pancakes(line)))
    i += 1
