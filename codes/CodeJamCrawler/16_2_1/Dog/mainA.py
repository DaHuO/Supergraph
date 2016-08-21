#! /usr/bin/env python3

import sys

words = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
letters = set(l for w in words for l in w)
count = dict((l, set()) for l in letters)
for i in range(10):
    for l in words[i]:
        count[l].add(i)

def solve(problem):
    found = list()
    problem = list(problem)
    problem.sort(key=(lambda l: len(count[l])))
    while problem:
        numbers = set(range(10))
        for i in range(10):
            if not all(l in problem for l in words[i]):
                numbers.remove(i)

        for l in problem:
            numbers.intersection_update(count[l])
            if len(numbers) == 1: break
            if len(numbers) == 0: raise ValueError()

        found.append(numbers.pop())
        for l in words[found[-1]]:
            problem.remove(l)

    return ''.join(map(str, sorted(found)))

def parse(case):
    return case

#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    with open(filename+'.out', 'w') as out:
        for (i, case) in enumerate(content.split('\n')[1:], 1):
            problem = parse(case)
            s = solve(problem)
            for o in [sys.stdout, out]:
                print('Case #', i, ': ', s, sep='', file=o)
