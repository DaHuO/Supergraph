#!/usr/bin/python3

import sys
import itertools

test = []

def recurse(word='', c=''):
    return (c + word, word + c)

def solve(word, rem=''):
    global test
    if not word:
        test.append(rem)
        return rem
    return list(map(lambda x: solve(word[1:], ''.join(x)), recurse(word[0], rem)))

check = True
number_of_test_cases = 0
i = 1

for line in sys.stdin:
    if check:
        number_of_test_cases = line.strip()
        check = False
        continue
    initial = line.strip()
    got = solve(initial)
    got = sorted(test)[-1]
    print("Case #{0}: {1}".format(i, got))
    test = []
    i += 1


# 'CAB'
