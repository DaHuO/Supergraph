#!/usr/bin/env python

import sys

def flip(p):
    return "".join(['+' if x == '-' else '-' for x in p[::-1]])

def helper(pancakes):
    flips = 0
    all_pancakes = set()
    all_pancakes.add(pancakes)
    goal = '+'*len(pancakes)
    pancakes_seen = set()
    pancakes_seen = pancakes_seen.union(all_pancakes)

    while True:
        if goal in all_pancakes:
            return flips
        flips += 1
        all_pancakes_after_flip = set()
        for pancakes in all_pancakes:
            for i in xrange(1,len(pancakes)+1):
                new_pancakes = flip(pancakes[:i]) + pancakes[i:]
                if new_pancakes not in pancakes_seen:
                    all_pancakes_after_flip.add(new_pancakes)

        all_pancakes = all_pancakes_after_flip
        pancakes_seen = pancakes_seen.union(all_pancakes)
        #print flips, len(pancakes_seen), len(all_pancakes)

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
    pancakes = test[0]
    sol = helper(pancakes)
    print 'Case #{}: {}'.format(case+1, sol)
