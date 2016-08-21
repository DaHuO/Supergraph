# can number of groups change on revert?
#
# [xAy]zB
# [(-y)(A^-1)(-x)]zB
#
# 1. Number of groups within xAy can't change as we don't change their order in meaningful way.
# 2. Number of overall groups might change if -x has the same sign as z.
#    In that case number of groups is lowered by 1.
import sys
from itertools import groupby

def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    numbers = line.strip().split()
    return [int(n) for n in numbers]


def solve(pancakes):
    groups = list(groupby(pancakes))
    if groups[-1][0] == '+':
        # don't need to rotate for the last group
        return len(groups) - 1
    return len(groups)


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        pancakes = sys.stdin.readline().strip()
        print "Case #%d: %d" % (t + 1, solve(pancakes))
