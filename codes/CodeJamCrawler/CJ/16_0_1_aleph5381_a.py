#!/usr/bin/env python3

import sys
rl = lambda: sys.stdin.readline()
T = int(rl())

def solve(casei):
    line = rl().split()
    N = int(line[0])
    if N is 0:
        print("Case #{}: INSOMNIA".format(casei))
        return
    check = [0] * 10
    x = 0
    fin = False
    while fin is False:
        x += N # x == ans*N
        tmp = x
        while tmp > 0:
            check[tmp%10] = 1
            tmp = tmp // 10
        fin = True
        for i in range(10):
            if check[i] == 0:
                fin = False
                break
    print("Case #{}: {}".format(casei, x))

for i in range(1, T+1):
    solve(i)
