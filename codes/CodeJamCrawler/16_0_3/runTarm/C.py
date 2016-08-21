import math
def find_divisor(n):
    if n % 2 == 0 and n > 2:
        return 2

    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    return 0

def from_base(s, base):
    return reduce(lambda a, c: a * base + int(c), s, 0)

def solve(N, J):
    fmt = '1{{:0{}b}}1'.format(N - 2)
    j = 0
    for i in xrange(0, 2**(N-2)):
        candidate = fmt.format(i)
        divisors = [find_divisor(from_base(candidate, k)) for k in xrange(2, 11)]
        if not all(divisors):
            continue

        print candidate, ' '.join(map(str, divisors))
        j += 1
        if j == J:
            break

import sys
sys.stdin = open('C-small.in', 'rt')
sys.stdout = open('C-small.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    print "Case #%d:" % t
    N, J = map(int, raw_input().strip().split(' '))
    solve(N, J)
