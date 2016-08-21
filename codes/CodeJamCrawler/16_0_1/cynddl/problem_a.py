#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve_sheep(n):
    if n == 0:
        return "INSOMNIA"

    k = 0
    visited = set()
    while True:
        k += n
        visited.update(str(k))

        if len(visited) == 10:
            return k


if __name__ == "__main__":
    nb_cases = int(input())

    for i in range(nb_cases):
        rv = solve_sheep(int(input()))

        print("Case #{}: {}".format(i + 1, rv))
