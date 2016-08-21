#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def counted_all(memo):
    for result in memo:
        if not result:
            return False
    return True


def mark(number, memo):
    r = number % 10
    memo[r] = True
    q = number // 10
    while q != 0:
        r = q % 10
        memo[r] = True
        q = q // 10


def solve(n):
    if n == 0:
        return 0
    counted = [False for _ in range(10)]
    current = n
    mark(current, counted)
    while not counted_all(counted):
        current += n
        mark(current, counted)
    return current


if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        result = solve(int(input()))
        if result == 0:
            print('Case #{}: {}'.format(t, 'INSOMNIA'))
        else:
            print('Case #{}: {}'.format(t, result))
