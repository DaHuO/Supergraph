#!/usr/bin/env python3

T = int(input())

def flip(pancakes):
    pancakes = list(pancakes[::-1])
    new_value = {'-': '+', '+': '-'}
    for i in range(len(pancakes)):
        pancakes[i] = new_value[pancakes[i]]
    return ''.join(pancakes)

def get_num_flips(pancakes):
    if not '-' in pancakes:
        return 0
    if not '+' in pancakes:
        return 1

    while pancakes[-1] == '+':
        pancakes = pancakes[:-1]
    assert '-' in pancakes, 'we do have minuses'

    num_initial_plusses = 0
    while pancakes[num_initial_plusses] == '+':
        num_initial_plusses += 1

    num_flips = 0
    if num_initial_plusses > 0:
        end = pancakes[num_initial_plusses:]
        start = flip(pancakes[:num_initial_plusses])
        pancakes = start + end
        num_flips += 1

    pancakes = flip(pancakes)
    num_flips += 1

    return num_flips + get_num_flips(pancakes)

for case in range(1, T+1):
    pancakes = input().strip()
    answer = get_num_flips(pancakes)
    print('Case #{}: {}'.format(case, answer))
