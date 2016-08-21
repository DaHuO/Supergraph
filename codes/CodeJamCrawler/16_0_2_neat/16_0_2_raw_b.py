#!/usr/bin/python3

from itertools import groupby

for i in range(1, 1+int(input())):
    print('Case #{}: '.format(i), end='')
    flip_count = 0
    for group, _ in groupby(reversed(input())):
        if (group == '-') != (flip_count % 2):
            flip_count += 1
    print(flip_count)
