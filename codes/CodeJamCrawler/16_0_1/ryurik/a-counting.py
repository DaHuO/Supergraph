#!/usr/bin/python3

import sys

def split_digits(n):
    result = set()
    while n >= 10:
        result.add(n % 10)
        n //= 10
    result.add(n)
    return result

def solve(n):
    result = n
    if result <= 0:
        return 'INSOMNIA'
    visited = split_digits(result)
    while len(visited) < 10:
        result += n
        visited = visited.union(split_digits(result))
    return str(result)

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for t in range(1, T + 1):
        N = int(sys.stdin.readline())
        print('Case #%d: %s' % (t, solve(N)))
