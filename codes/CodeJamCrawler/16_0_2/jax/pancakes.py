#!/usr/bin/python
import sys

HAPPY = '+'
BLANK = '-'


def output(case_nr, result):
    case_nr = str(case_nr)
    result = str(result)
    sys.stdout.write("Case #{}: {}\n".format(case_nr, result))


def flip():
    cases = int(sys.stdin.readline().strip())
    for i in xrange(cases):
        pancakes = list(sys.stdin.readline().strip())

        nr_flips = 0
        if pancakes[-1] == BLANK:
            nr_flips += 1
        
        if len(pancakes) > 1:
            for x in xrange(len(pancakes) - 2, -1, -1):
                if pancakes[x] != pancakes[x + 1]:
                    nr_flips += 1
        output(i + 1, nr_flips)

if __name__ == '__main__':
    flip()

