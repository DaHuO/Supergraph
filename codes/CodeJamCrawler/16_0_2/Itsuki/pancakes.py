#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check(pancakes):
    for pancake in pancakes:
        if pancake == '-':
            return False
    return True


def flip(pancakes):
    start = pancakes[0]
    new_mark = '+' if start == '-' else '-'
    pancakes[0] = new_mark
    for i in range(1, len(pancakes)):
        current = i
        if pancakes[current] != start:
            break
        pancakes[i] = new_mark


def solve(pancakes):
    count = 0
    while not check(pancakes):
        flip(pancakes)
        count += 1
    return count


if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        data = input()
        initial_pancakes = [data[i] for i in range(len(data))]
        print('Case #{}: {}'.format(t, solve(initial_pancakes)))
