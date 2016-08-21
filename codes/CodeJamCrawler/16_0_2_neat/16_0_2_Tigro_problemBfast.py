#! /usr/bin/python3

T = int(input())

for i in range(T):
    stack = input()

    howManyGroups = 0

    # Removing right pancakes from the bottom
    stack = stack.rstrip('+')

    if len(stack) > 0:
        curSign = '.'

        for pancake in stack:
            if pancake != curSign:
                curSign = pancake
                howManyGroups += 1

    print("Case #%i: %i" % (i+1, howManyGroups))