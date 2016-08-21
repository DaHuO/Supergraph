#!/usr/bin/python3

def read(): return tuple(map(int, input().split()))

def solve():
    s = list(input())
    ans = 0
    while True:
        while s and s[-1] == '+':
            s.pop()
        if not s:
            return ans
        ans += 1
        if s[0] == '-':
            s = ['+' if _ == '-' else '-' for _ in reversed(s)]
        else:
            i = 0
            while s[i] == '+' and i < len(s):
                i += 1
            s = ['+' if _ == '-' else '-' for _ in reversed(s[:i])] + s[i:]

if __name__ == '__main__':
    for _ in range(int(input())):
        print('Case #%i: %i' % (_ + 1, solve()))
