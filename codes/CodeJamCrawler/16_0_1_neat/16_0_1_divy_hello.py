import math
import sys

def count_sheep(n, arr, val):
    done = True
    new_arr = arr
    x = val * n
    y = len(str(x))
    if y != 0:
        b = x
        for z in range(1,y+1):
            a = b % 10
            new_arr[a] = True
            b = b / 10
    for exist in new_arr :
        done = done and exist
    if n == 200 and not done:
        return "INSOMNIA"
    if done:
        res = str(x)
        return res
    else:
        return count_sheep(n+1, new_arr, val)

testCases = int(input())

for testCase in range(1, testCases + 1):
    newTC = int(input())
    arr = [False] * 10
    print "Case #" + str(testCase) + ": " + count_sheep(1, arr, newTC)
