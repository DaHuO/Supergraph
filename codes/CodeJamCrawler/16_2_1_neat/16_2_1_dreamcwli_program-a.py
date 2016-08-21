#!/usr/bin/env python

from __future__ import print_function

words = {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE'
}

first_filters = {
    'Z': 0,
    'W': 2,
    'U': 4,
    'X': 6,
    'G': 8
}

second_filters = {
    'O': 1,
    'T': 3,
    'F': 5,
    'S': 7
}

third_filters = {
    'I': 9
}

cases = raw_input()
cases = int(cases)

for case in range(1, cases + 1):
    string = raw_input()
    length = len(string)
    counts = {}
    for i in range(length):
        character = string[i]
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    results = {}
    for i in range(10):
        results[i] = 0

    for filters in (first_filters, second_filters, third_filters):
        for key in filters:
            try:
                count = counts[key]
            except KeyError:
                continue
            if not count:
                continue
            index = filters[key]
            word = words[index]
            length = len(word)
            for i in range(length):
                character = word[i]
                counts[character] -= count
            results[index] += count

    print('Case #%d: ' % case, end='')
    for i in range(10):
        result = results[i]
        for j in range(result):
            print(i, end='')
    print()
