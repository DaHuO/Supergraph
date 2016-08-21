#!/usr/bin/python3

import sys

def f(n):
    if n == 0:
        return "INSOMNIA"

    ans = set([str(x) for x in range(0, 10)])

    for t in range(1, 1000001):
        q = t * n
        for digit in str(q):
            if digit in ans:
                ans.remove(digit)
        if not ans:
            return str(q)


def main():
    n = int(input())
    for i in range(1, int(n) + 1):
        line = input()
        line = line.strip()
        print("Case #" + str(i) + ": " + f(int(line)))
        n = n + 1


if __name__ == "__main__":
    main()
