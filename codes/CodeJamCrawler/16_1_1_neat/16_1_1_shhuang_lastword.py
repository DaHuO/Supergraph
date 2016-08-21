#!/usr/bin/env python

import sys

def helper(word):
    last_word = word[0]
    for l in list(word[1:]):
        if l < last_word[0]:
            last_word = last_word + l
        else:
            last_word = l + last_word

    return last_word

def parse_file(num_lines=-1):
    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    i = 1
    tests = []
    varying_nlines = False
    if num_lines == -1:
        varying_nlines = True

    while i < len(lines):
        new_test = []
        if varying_nlines:
            num_lines = int(lines[i])
            i += 1

        for j in range(num_lines):
            new_test.append(lines[i])
            i += 1
        tests.append(new_test)
    return int(lines[0]), tests

num_tests, tests = parse_file(num_lines=1)
#num_tests, tests = parse_file()

for case,test in enumerate(tests):
    sol = helper(test[0])
    print 'Case #{}: {}'.format(case+1, sol)
