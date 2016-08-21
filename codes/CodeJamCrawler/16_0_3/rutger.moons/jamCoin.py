__author__ = 'rutger'
import math

def generatePrimes(nb):
    max = math.floor(math.sqrt(nb)) + 1
    b = [False, False, True] + [True, False]*math.ceil((nb/2)-1)
    i = 3
    while (i < max):
        if b[i]:
            j = 2*i
            while (j <= nb):
                b[j] = False
                j += i
        i += 1

    return b

n = 32
j = 500

primes = generatePrimes(2**16)

def convertToBase(a, base):
    total = 0
    x = 1
    i = len(a) - 1
    while i >= 0:
        total += a[i] * x
        x *= base
        i -= 1
    return total

def increment(a):
    i = len(a) - 1
    while i > 0:
        a[i] = not a[i]
        if a[i]:
            break
        i -= 1
    return a


def findDivisor(n):
    if n < len(primes) and primes[n]:
        return 0

    #not a prime:
    if n % 2 == 0:
        return 2
    for i in range(3, 50000, 2):
        if n % i == 0:
            return i
    return -1

def isJamCoin(x):
    if not x[0] or not x[-1]:
        return False, []
    divisors = []
    for base in range(2, 11):
        d = findDivisor(convertToBase(x, base))
        if d <= 0:
            return False, divisors
        divisors.append(d)
    return True, divisors


def toResult(a, divisors):
    number = ""
    for i in a:
        if i:
            number += "1"
        else:
            number += "0"

    divString = ""
    for divisor in divisors:
        divString += " " + str(divisor)
    return number + divString

#VERGEET INPUT NIET!!
input()
input()

print("Case #1:")

count = 0
b = [True] + (n - 1) * [False]
while count < j:
    bool, d = isJamCoin(b)
    if bool:
        count += 1
        print(toResult(b, d))
    b = increment(b)
