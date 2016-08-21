#!/usr/bin/env python3

cases = int(input())

for i in range(cases):
    count = 0
    stack = input()
    prev = stack[0]
    for pancake in stack:
        if pancake != prev:
            prev = pancake
            count += 1
    if stack[-1] == '-':
        count += 1

    print("Case #{}: {}".format(i+1, count))
