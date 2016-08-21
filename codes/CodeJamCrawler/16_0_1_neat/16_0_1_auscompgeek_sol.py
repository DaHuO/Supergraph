#!/usr/bin/env python3


def solve(N):
    if not N:
        return 'INSOMNIA'
    digits = set()
    n = 0
    while len(digits) != 10:
        n += N
        a = n
        while a:
            a, b = divmod(a, 10)
            digits.add(b)
    return n


def main():
    T = int(input())
    for x in range(1, T+1):
        print('Case #{}: {}'.format(x, solve(int(input()))))


if __name__ == "__main__":
    main()
