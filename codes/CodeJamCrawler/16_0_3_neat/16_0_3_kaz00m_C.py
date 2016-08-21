#!/usr/bin/env python


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 2:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def getNonTrivialDivisor(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return i

infile = open('C-small.in')
outfile = open('C-large.out', 'w')
print >>outfile, "Case #1:"
t = int(infile.readline().strip())
num = infile.readline().strip().split(' ')
n = int(num[0])
x = n - 2
j = int(num[1])

count = 0

for i in xrange(1, 2**x - 1):
    number = '1{:0{x}b}1'.format(i, x=x)
    isJamCoin = True
    for i in xrange(2, 11):
        num = int(number, i)
        if isPrime(num):
            isJamCoin = False
            break
    if isJamCoin:
        print >>outfile, number + number + " ",
        for i in xrange(2, 11):
            print >>outfile, getNonTrivialDivisor(
                int(number + number, i)), " ",
        print >>outfile, '\n',
        count += 1
    if count == j:
        break
