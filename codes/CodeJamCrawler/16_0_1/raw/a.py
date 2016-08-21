#!/usr/bin/python3

from collections import defaultdict
from itertools import count

for i in range(1, 1+int(input())):
    print('Case #{}: '.format(i), end='')
    n = int(input())
    if n == 0:
        print('INSOMNIA')
        continue
    seen = defaultdict(bool)
    for number in (n*x for x in count(1)):
        for digit in map(int, str(number)):
            seen[digit] = True
        if all(seen[digit] for digit in range(10)):
            print(number)
            break
