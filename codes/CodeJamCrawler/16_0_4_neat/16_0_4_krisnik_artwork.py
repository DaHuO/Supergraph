__author__ = 'KH2006'

import math

def listToString(listOfNumbers):
    result = str(listOfNumbers[0])
    for i in range(1, len(listOfNumbers)):
        result = result + " " + str(listOfNumbers[i])

    return result

t = int(input())  # read a line with a single integer
for testCase in range(1, t + 1):
    k, c, s = [int(s) for s in input().split(" ")]
    output = []

    if s == k:
        output = []
        for s1 in range(1,s+1):
            output.append(s1)
    elif s > k/2:

        totalLen = math.pow(k,c)
        pos = 2
        for s1 in range(1, s+1):
            output.append(pos)
            pos = pos + k + 1

    if len(output) == 0:
        output = "IMPOSSIBLE"
    else :
        output = listToString(output)

    print("Case #{}: {}".format(testCase, output))