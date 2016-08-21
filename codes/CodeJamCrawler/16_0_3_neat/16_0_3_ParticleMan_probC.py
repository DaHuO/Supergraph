#!/usr/bin/env python

rformat = "{} " * 9 + "{}"
def printResult(s, factors):
    print rformat.format(s, *factors)

def toInt(s, base):
    curr = 1
    retval = 0
    for x in s[::-1]:
        retval += int(x) * curr
        curr *= base
    return retval

def toStr(n, base):
    retval = ''
    while n > 0:
        retval = str(n%base) + retval
        n /= base
    return retval

def getValues(s):
    values = []
    for base in range(2,11):
        values.append(toInt(s, base))
    return values

def findFactor(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return f
        if n % (f+2) == 0:
            return f+2
        f += 6
        if f == 60005:
            return -2
    return -1

t = int(raw_input())
N,J = [int(s) for s in raw_input().split(" ")]
startStr = '1' + ('0' * (N-2)) + '1'
found = 0
n = toInt(startStr, 2)
print "Case #1:"
while found < J:
    s = toStr(n, 2)
    values = getValues(s)
    factors = [findFactor(x) for x in values]
    if -2 in factors:
        pass
    elif -1 not in factors:
        printResult(s, factors)
        found += 1
    n += 2
