#!/usr/bin/env python3

def solve(n):
    if (n == 0):
        print("INSOMNIA")
    else:
        digits = set('0123456789')
        i = 0
        while digits:
            i += 1
            digits.difference_update(set(str(i * n)))
        print(i * n)

if __name__ == '__main__':
    for idx in range(1, int(input())+1):
        n = int(input())
        print("Case #{}: ".format(idx), end='')
        solve(n)
