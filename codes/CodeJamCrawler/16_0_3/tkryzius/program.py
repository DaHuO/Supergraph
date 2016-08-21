import math

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

#calculates primes
primes = [2]
for z in xrange(3, 1000):
    isPr = True
    for p in primes:
        if z%p == 0:
            isPr = False
            break
    if isPr:
        primes += [z]
print 'Primes calculated'        

def toBase(jamcoin, base):
    jamcoin = jamcoin[::-1]
    result = 0
    multiplier = 1
    for i in jamcoin:
        result += int(i)*multiplier
        multiplier *= base
    return result

def isPrime(n):
    global primes
    for i in primes:
        if n == i:
            return True
        if n%i == 0:
            return False
    return True

def getDivisor(n, divisors):
    div = set(divisors)
    for i in xrange(2, min(1000000, int(math.sqrt(n))) + 1):
        if n%i == 0 and i not in div:
            return i
    return 0

for i in xrange(t):
    fout.write('Case #' + str(i + 1) + ':' + '\n')
    n, j = map(int, fin.readline().split())
    number = 0
    max = (n-2)**2
    while number <= max and j > 0:
        binary = bin(number)[2:]
        l = n - len(binary) - 2
        if l > 0:
            binary = '0'*l + binary
        jamcoin = '1' + binary + '1'
        divisors = []
        for base in xrange(2, 11):
            nBase = toBase(jamcoin, base)
            if isPrime(nBase):
                break
            div = getDivisor(nBase, divisors)
            if div == 0:
                break
            divisors += [div]
        if len(divisors) == 9:
            j -= 1
            fout.write(jamcoin + ' ' + ' '.join(map(str, divisors)) + '\n')
        number += 1

fout.close()

print 'FINISHED'
