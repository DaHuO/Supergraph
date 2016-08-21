#!/usr/bin/python

from __future__ import print_function

T = int(raw_input())
for t in range(1, T + 1):
    pancakes = [c == '+' for c in str(raw_input().strip())]
    steps = 0
    print('Case #', t, ': ', sep='', end='')
    while not all(pancakes):
        left, right = 0, len(pancakes) - 1
        while left < len(pancakes) and not pancakes[left]:
            left += 1
        while right > 0 and pancakes[right]:
            right -= 1

        right += 1

        if left != 0:
            pancakes[0:left] = [True] * (left)
            steps += 1

        if right > left:
            pancakes[0:right] = reversed(pancakes[0:right])
            steps += 1

    print(steps)
