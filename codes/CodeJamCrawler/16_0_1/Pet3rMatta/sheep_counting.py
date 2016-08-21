#!/usr/bin/env python3

in_file = open('A-large.in.txt', 'r')

for case in range(1, int(in_file.readline().strip()) + 1):

    digits = [False for _ in range(10)]

    n = int(in_file.readline().strip())

    if n:
        i = 0
        while sum(digits) < 10:
            i += 1
            for digit in list(set(str(n * i))):
                digits[int(digit)] = True

        print('Case #{}: {}'.format(case, n * i))
    else:
        print('Case #{}: INSOMNIA'.format(case))
