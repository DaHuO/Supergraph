from sys import stdin
from operator import mul
from itertools import product

def binstrs(n):
    return ('1' + ''.join(x) + '1' for x in product('01', repeat=n))

def divisor(n):
    if n == 2 or n == 3:
        return 0
    if n < 2 or n%2 == 0:
        return n//2
    if n < 9:
        return 0
    if n%3 == 0:
        return n//3
    for i in xrange(5,int(n**0.5)+2, 6):
        if n%i == 0: return i
        elif n%(i+2) == 0: return i + 2
    return 0

for t in range(1, int(stdin.readline()) + 1):
    [n, j] = map(int, stdin.readline().split())
    print 'Case #%d:' % t
    for s in binstrs(n-2):
        if j == 0:
            break
        divs = [divisor(int(s, b)) for b in range(2, 11)]
        if reduce(mul, divs) != 0:
            print s, ' '.join(map(str, divs))
            j -= 1
