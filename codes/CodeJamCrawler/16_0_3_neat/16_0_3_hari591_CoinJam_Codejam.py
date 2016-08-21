import math


length = 16
total = 50

def getBinaryRep(n, b):
    a = str(baseN(n, b))
    temp = length - len(a) - 2
    return ('0'* temp) + a

def checkNotPrime(n):
    if n in [2, 3, 5, 7]:
        return 0
    if n % 6 == 1 or n %6 == 5:
        if n %2 and n%3 and n%5 and n%7:
            t = 2

            while True:
                if (6 * t) + 1 > math.sqrt(n):
                    return 0
                div = 6 * t
                if n % (div + 1) == 0:
                    return div + 1
                if n % (div - 1) == 0:
                     return div - 1
                t += 1

    return -1

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def getDivisor(n):
    d = 2
    while d  < n and n % d != 0:
        d += 1
    if n ==d:
        return 0
    return d

raw_input()
raw_input()

print "Case #1: "

i = 0
j = 0
while j < total:
    num = "1" + getBinaryRep(i, 2) + "1"
    output = num + " "

    t = 2
    failed = 0
    while t < 11:
        tempNum = int(num, t)
        temp = checkNotPrime(tempNum)
        if temp == 0:
            failed = 1
            break
        elif temp == -1:
            output += str(getDivisor(tempNum)) + " "

        else:
            output += str(temp) + " "

        t += 1
    if not failed:
        j += 1
        print output
    i += 1
