#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals


def count_sheep(n):
    seen = {
        str(digit): False
        for digit in range(10)
    }
    count = 1
    last = 0
    current = n
    while last != current:
        digits = list(str(current))
        for digit in digits:
            if not seen[digit]:
                seen[digit] = True
        if all(seen.values()):
            return current
        else:
            last = current
            count += 1
            current = count * n
    return 'INSOMNIA'


def main():
    num_cases = int(raw_input())
    for i in range(num_cases):
        current = raw_input()
        result = count_sheep(int(current))
        print('Case #{num}: {result}'.format(num=i+1, result=result))

if __name__ == '__main__':
    main()
