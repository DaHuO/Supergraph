import sys

def primes(n):
    res = []
    if n > 2:
        res.append(2)
    for x in xrange(3, n + 1, 2):
        is_prime = True
        for n in xrange(2, int(x**0.5) + 2):
            if x%n == 0:
                is_prime = False
                break
        if is_prime:
            res.append(x)
    return res

first_primes = primes(1000000)

def first_div(n):
    for d in first_primes:
        if d >= n:
            break
        if n % d == 0:
            return d

lines = open(sys.argv[1], "rb").read().splitlines()
t = int(lines[0])
res = []

for i in xrange(1, t + 1):
    res.append("Case #%d:\n" % (i,))
    n, j = map(int, lines[i].split())
    total = 0

    for y in xrange(0, 2**(n - 2)):
        x = ''
        for k in xrange(n - 2):
            x = str(y % 2) + x
            y /= 2
        x = '1' + x + '1'

        divs = []
        for base in xrange(2, 11):
            num = int(x, base)
            d = first_div(num)
            if d is not None:
                divs.append(d)
            else:
                break
        if len(divs) == 9:
            total += 1
            res.append("%s %s\n" % (x, ' '.join(map(str, divs))))
        if total == j:
            break

open(sys.argv[2], "wb").write(''.join(res))
