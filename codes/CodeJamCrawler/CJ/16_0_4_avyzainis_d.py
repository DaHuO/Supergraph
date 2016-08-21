#!/usr/bin/env python3

T = int(input())


for testCase in range(T):
    K, C, S = input().split()
    K, C, S = int(K), int(C), int(S)

    if S == K:
        print("Case #{}: {}".format(testCase + 1, ' '.join([str(number + 1) for number in range(K)])))
