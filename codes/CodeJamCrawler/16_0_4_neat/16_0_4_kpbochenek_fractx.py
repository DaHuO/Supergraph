#!/bin/python

T = int(input())

for i in range(T):
    K, C, S = list(map(int, input().split()))

    if S == K:
        result = ""
        for j in range(S):
            result += str(j + 1) + " "
    else:
        result = "IMPOSSIBLE"

    print("Case #" + str(i+1) + ": " + result)
