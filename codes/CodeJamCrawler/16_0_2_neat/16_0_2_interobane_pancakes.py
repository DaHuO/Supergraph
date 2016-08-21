#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals


def pancakes(stack):
    count = 0
    while True:
        flip_index = ''.join(stack).rfind('-')
        if -1 == flip_index:
            return count
        count += 1
        stack = ['+' if ch == '-' else '-' for ch in stack[:flip_index]]


def main():
    num_cases = int(raw_input())
    for i in range(num_cases):
        stack = raw_input()
        result = pancakes(stack)
        print('Case #{num}: {result}'.format(num=i+1, result=result))

if __name__ == '__main__':
    main()
