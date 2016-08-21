#!/usr/bin/python3

import sys

def flip(ch):
    if ch == '-':
        return '+'
    elif ch == '+':
        return '-'


def f(cakes):
    n = 0
    wanted = '-'

    for ch in cakes[::-1]:
        if ch == wanted:
            n = n + 1
            wanted = flip(wanted)

    return n


def main():
    n = int(input())
    for i in range(1, int(n) + 1):
        line = input()
        line = line.strip()
        ans = f(line)
        print("Case #" + str(i) + ": " + str(ans))
        n = n + 1


if __name__ == "__main__":
    main()
