#!/usr/bin/env python3
import string
import itertools
import sys

sys.setrecursionlimit(2000)


def is_equal_rule(party_dict):
    return max(party_dict.values()) <= sum(party_dict.values()) / 2


def solve_bruteforce(party_dict):
    if not party_dict:
        return []
    choices = list(map(''.join, itertools.combinations(party_dict.keys(), 2))) + [key * 2 for key, val in party_dict.items() if val > 1] + list(party_dict.keys())
    for choice in choices:
        new_party_dict = dict(party_dict)
        for p in choice:
            if new_party_dict[p] > 1:
                new_party_dict[p] -= 1
            else:
                del new_party_dict[p]
        if new_party_dict and is_equal_rule(new_party_dict) or not new_party_dict:
            return [choice] + solve_bruteforce(new_party_dict)
    return []


def solve(T, N, P):
    party_dict = {string.ascii_uppercase[i]: P[i]
                  for i in range(N)}
    instructions = solve_bruteforce(party_dict)

    result = ' '.join(instructions)
    print('Case #{}: {}'.format(T, result))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for case in range(n_cases):
        N = int(sys.stdin.readline().strip())
        P = list(map(int, sys.stdin.readline().strip().split()))
        solve(case + 1, N, P)


if __name__ == '__main__':
    main()
