#!/bin/python3

def solve():
    T = int(input())
    for t in range(1, T+1):
        print("Case #{0}:".format(t))
        N , J = map(int, input().split())
        for i in range(J):
            v = i+1
            str1 = bin(v)[2:]+"1"
            jamcoin = str1 + ("0" * (N - 2*len(str1))) + str1
            ans = jamcoin
            for i in range(2, 11):
                ans += " " + str(int(str1, i))
            print(ans)

solve()
