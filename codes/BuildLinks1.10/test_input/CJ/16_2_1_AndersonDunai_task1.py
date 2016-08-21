#!/usr/bin/env python2

import sys


DIGITS = [
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
]


# def has(sentence, word):
#     copy = sentence[::]
#     for c in word:
#         try:
#             copy.remove(c)
#         except:
#             pass
#     return len(copy) == len(sentence) - len(word)


def process(source, history):
    results = []
    for i, word in enumerate(DIGITS):
        # if sentence.
        # possible = sentence
        copy = source[::]
        for c in word:
            try:
                copy.remove(c)
            except:
                pass
        if len(copy) == len(source) - len(word):
            # Letter removed!
            if len(copy) == 0:
                results = results + [history + [i]]
            else:
                results = results + process(copy, history + [i])
    return [x for x in results if x]


def solve(sentence):
    # sentence = list(sentence)
    # print has(sentence, 'THREE')
    sentence = sorted(list(sentence))

    results = process(sentence, [])
    return ''.join([str(x) for x in results[0]])



count = int(sys.stdin.readline().strip())

current = 1

while current <= count:
    print 'Case #{}: {}'.format(current, solve(sys.stdin.readline().strip()))
    current += 1
