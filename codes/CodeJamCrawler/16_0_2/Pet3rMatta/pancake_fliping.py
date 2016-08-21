#!/usr/bin/env python3

in_file = open('B-large.in.txt', 'r')

for case in range(1, int(in_file.readline().strip()) + 1):

    pancakes = in_file.readline().strip()

    flips = 1 if pancakes[0] is '-' else 0
    for i in range(1, len(pancakes)):
        if pancakes[i] is not pancakes[i - 1] and pancakes[i] is '-' and pancakes[i - 1] is '+':
            flips += 2

    print('Case #{}: {}'.format(case, flips))
