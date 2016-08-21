#!/usr/bin/python

cc = int(raw_input())

for c in range(1, cc+1):
    stack = raw_input()
    curr = stack[0]
    swaps = 0
    for it in stack:
        if not curr == it:
            swaps += 1
            curr = it

    if curr.endswith("+"):
        print "Case #" + str(c) + ": " + str(swaps)
    else:
        print "Case #" + str(c) + ": " + str(swaps+1)
