from sys import stdin
from itertools import permutations

def play(string, pos = 0, current = ''):
    if pos > len(string) - 1:
        yield current
        return

    next = current + string[pos]
    for x in play(string, pos + 1, next):
        yield x

    if pos <= 0:
        return

    prev = string[pos] + current
    for x in play(string, pos + 1, prev):
        yield x

test_cases = raw_input()
for i, line in enumerate(stdin, 1):
    line = line.strip()
    print "Case #%d:"%i, sorted(map(lambda x: ''.join(x), play(line)))[-1]
