from sys import stdin
from itertools import groupby

def solve(pancakes):
    compact = ''.join(c for c, _ in groupby(pancakes))

    if compact[0] == '+':
        return 2 * compact.count('-')
    else:
        return 2 * compact.count('-') - 1

T = int(stdin.readline())

for i in range(1, T + 1):
    print('Case #{}:'.format(i), solve(stdin.readline().strip()))
