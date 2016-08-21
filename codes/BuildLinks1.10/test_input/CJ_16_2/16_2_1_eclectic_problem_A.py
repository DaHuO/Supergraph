#!/usr/bin/python3
# import sys
# import numpy as np

T = int(input())

for i_T in range(T):
    S = list(input())
    S.sort()
    # print(i_T, S)
    numbers = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    occurences = [0]*10
    occurences[0] = S.count('Z')
    occurences[2] = S.count('W')
    occurences[4] = S.count('U')
    occurences[6] = S.count('X')
    occurences[8] = S.count('G')
    res = list()
    for i, n in enumerate(occurences):
        # print(i, n)
        for j in range(n):
            for letter in numbers[i]:
                # print(i, n, letter)
                S.remove(letter)
        occurences[i] = 0
        res.extend([i]*n)
    # print('FIRST', S, occurences, res)

    occurences[1] = S.count('O')
    occurences[3] = S.count('T')
    occurences[5] = S.count('F')
    occurences[7] = S.count('S')
    for i, n in enumerate(occurences):
        # print(i, n)
        for j in range(n):
            for letter in numbers[i]:
                S.remove(letter)
        occurences[i] = 0
        res.extend([i]*n)
    # print(len(S), S, res)
    # print('SECOND', S, occurences, res)
    occurences[9] = S.count('I')
    # print('THIRD', S, occurences, res)
    res.extend([9]*occurences[9])
    res.sort()
    result = ''.join(['%d'%e for e in res])
    # N, M = tuple(map(int, input().split(" ")))
    print("Case #{}: {}".format(i_T+1, result))
