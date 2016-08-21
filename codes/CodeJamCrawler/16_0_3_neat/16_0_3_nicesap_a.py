#!python

import primefac

f = open("input.txt")
lines = f.readlines()

(n, x) = lines[1].split()

n = int(n)
x = int(x)

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
        return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

for i in xrange(2**(n-1) + 1, 2**n, 2):
    s = baseN(i, 2)
    ok = True
    for j in range(2,11):
        w = int(s, j)
        if len(list(primefac.primefac(w))) == 1:
            ok = False
        if not ok:
            break
    if ok:
        x -= 1

        l = [s]
        for j in range(2, 11):
            l += [str(list(primefac.primefac(int(s, j)))[0])]

        print " ".join(l)

        if x == 0:
            break
