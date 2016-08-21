#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    T = int(input())
    for t in range(1, T+1):
        s = input().rstrip('+')
        cnt = 0
        while len(s) != 0:
            cnt += 1
            start = s.find('+')
            if start == -1:
                break
            elif start == 0:
                s = s[s.find('-'):][::-1]
            else:
                s = ('+' * start) + s[start:]
            s = s.rstrip('+')
        ans = cnt
        print("Case #{}: {}".format(t, ans))

if __name__ == "__main__":
    main()
