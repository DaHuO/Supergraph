#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        if N == 0:
            ans = "INSOMNIA"
        else:
            digits = {}
            n = 0
            while len(digits) != 10:
                n += 1
                for s in str(N * n):
                    digits[s] = 1
            ans = n * N
        print("Case #{}: {}".format(t, ans))

if __name__ == "__main__":
    main()
