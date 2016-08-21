from itertools import product, combinations
from math import floor, sqrt

def div(n):
    for i in range(2, int(floor(sqrt(n) + 1))):
        if n % i == 0:
            return i
    return None

def check(s):
    for b in range(2, 11):
        assert int(s, b) % (b + 1) == 0

def solve(n, j):
    found = 0
    odds = range(1, n - 1, 2)
    evens = range(2, n, 2)
    for a, b in product(combinations(odds, n / 4), combinations(evens, n / 4)):
        if found == j:
            break
        s = ''.join([
            '1' if i == 0 or i == n - 1 or i in set(a + b) else '0'
            for i in range(n)
        ])
        divs = check(s)
        print s, ' '.join(map(str, range(3, 12)))
        found += 1


print 'Case #1:'
T = input()
solve(*map(int, raw_input().strip().split()))
