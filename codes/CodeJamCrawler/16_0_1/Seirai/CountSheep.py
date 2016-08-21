#!/usr/bin/env python
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
completeArray = [0,1,2,3,4,5,6,7,8,9]
t = int(input())  # read a line with a single integer
for i in range(1, t+1):
    n = int(input())
    numHolder = []
    finalNumber = 0
    multiplier = 1
    temp = int(n)
    if n == 0:
        finalNumber = "INSOMNIA"
    else:
        while not (completeArray == numHolder):
            digitHolder = [int(x) for x in str(temp)]
            for stuff in digitHolder:
                if not (stuff in numHolder):
                    numHolder.append(stuff)
                    finalNumber = temp
                    #print ("{} is not in numholder!".format(stuff))
            temp = multiplier * n
            multiplier = multiplier + 1
            numHolder.sort()
    print("Case #{}: {}".format(i, finalNumber))
