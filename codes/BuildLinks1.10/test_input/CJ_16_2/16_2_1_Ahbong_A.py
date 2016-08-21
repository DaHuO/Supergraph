#!/usr/bin/env python3

import collections

N = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
NC = tuple(collections.Counter(n) for n in N)
U = (0, 2, 4, 6, 8, 3, 7, 1, 5, 9)


def match(counter, n):
    for char, count in NC[n].items():
        if counter[char] < count:
            return False
    for char, count in NC[n].items():
        counter[char] -= count
    return True


def solve(line):
    num_counter = collections.defaultdict(int)
    char_counter = collections.Counter(line)
    for u in U:
        while match(char_counter, u):
            num_counter[u] += 1
    return "".join(str(num) * times for num, times in sorted(num_counter.items()))


T = int(input())
for t in range(1, T + 1):
    line = input()
    ans = solve(line)
    print("Case #{}: {}".format(t, ans))
